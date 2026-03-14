#!/usr/bin/env python3
"""
render_cv.py
============
Compile cv.tex into:
  1. assets/pdf/CV_Behzad.pdf        (for the download button)
  2. _pages/cv.md                    (navigable web page)

Usage (run from repo root or from assets/cv_latex/):
    python assets/cv_latex/render_cv.py

Requirements:
    - pdflatex and bibtex installed (TeX Live / MiKTeX)
    - No extra Python packages needed (stdlib only)
"""

import re
import subprocess
import shutil
import sys
import tempfile
from pathlib import Path
from collections import defaultdict

# ── Paths (relative to this script's location) ────────────────────────────
HERE     = Path(__file__).parent
REPO     = HERE.parent.parent          # two levels up from assets/cv_latex/
CV_TEX   = HERE / "cv.tex"
BIB_FILE = HERE / "publications.bib"
PDF_OUT  = REPO / "assets" / "pdf" / "CV_Behzad.pdf"
MD_OUT   = REPO / "_pages" / "cv.md"

# Single bib source — the main site bib (richer metadata, used for both web page and PDF)
SITE_BIB = REPO / "_bibliography" / "papers.bib"


# ══════════════════════════════════════════════════════════════════════════
# LaTeX text utilities
# ══════════════════════════════════════════════════════════════════════════

def strip_latex_comments(text: str) -> str:
    """Remove % comments (but not escaped \\%)."""
    lines = []
    for line in text.split("\n"):
        cleaned = re.sub(r"(?<!\\)%.*", "", line)
        lines.append(cleaned)
    return "\n".join(lines)



# Mapping for LaTeX accent commands → Unicode (covers most CV/bib use-cases)
_ACCENT_MAP = {
    "'": {"a":"á","e":"é","i":"í","o":"ó","u":"ú","y":"ý",
          "A":"Á","E":"É","I":"Í","O":"Ó","U":"Ú","Y":"Ý",
          "\\i":"í"},             # \'{\i} = dotless-i with acute
    "`": {"a":"à","e":"è","i":"ì","o":"ò","u":"ù",
          "A":"À","E":"È","I":"Ì","O":"Ò","U":"Ù"},
    '"': {"a":"ä","e":"ë","i":"ï","o":"ö","u":"ü",
          "A":"Ä","E":"Ë","I":"Ï","O":"Ö","U":"Ü"},
    "^": {"a":"â","e":"ê","i":"î","o":"ô","u":"û",
          "A":"Â","E":"Ê","I":"Î","O":"Ô","U":"Û"},
    "~": {"n":"ñ","N":"Ñ","a":"ã","o":"õ","A":"Ã","O":"Õ"},
    "c": {"c":"ç","C":"Ç"},
    "v": {"s":"š","z":"ž","c":"č","S":"Š","Z":"Ž","C":"Č"},
    "l": {"":"ł"},
}

def _replace_accents(s: str) -> str:
    """Convert LaTeX accent commands to Unicode characters.

    Handles all common forms:
      \'{e}     →  é          (braced argument)
      \'e       →  é          (bare single-char argument)
      {\'e}     →  é          (grouped)
      \'{\i}    →  í          (braced special command)
      {\'\i}    →  í          (grouped special command)
    """
    for acc, table in _ACCENT_MAP.items():
        for base, uni in table.items():
            ea = re.escape(acc)
            eb = re.escape(base)
            # Form A: \acc{base}      e.g. \'{e} or \'{\i}
            s = s.replace(f"\\{acc}{{{base}}}", uni)
            # Form B: {\acc{base}}    e.g. {\'{\i}}
            s = s.replace(f"{{\\{acc}{{{base}}}}}", uni)
            # Form C: {\acc base}     e.g. {\'e} or {\'\i}
            s = s.replace(f"{{\\{acc}{base}}}", uni)
            # Form D: \acc base       bare (single char or \special)
            s = re.sub(rf"\\{ea}{eb}", uni, s)
    return s


def latex_to_md(s: str) -> str:
    """Best-effort conversion of LaTeX markup to Markdown."""
    if not s:
        return ""
    s = s.replace("\\newline", "\n")
    s = s.replace("\\\\", "\n")
    # Accented characters (must come before generic command stripping)
    s = _replace_accents(s)
    # Formatting
    s = re.sub(r"\\textit\{([^}]*)\}",  r"*\1*",    s)
    s = re.sub(r"\\textbf\{([^}]*)\}",  r"**\1**",  s)
    s = re.sub(r"\\emph\{([^}]*)\}",    r"*\1*",    s)
    s = re.sub(r"\\texttt\{([^}]*)\}",  r"`\1`",    s)
    # URLs / hyperlinks
    s = re.sub(r"\\url\{([^}]*)\}",                  r"[\1](\1)",   s)
    s = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}",      r"[\2](\1)",   s)
    # Special chars
    s = s.replace("\\$", "$").replace("\\%", "%").replace("\\&", "&")
    s = s.replace("\\{", "{").replace("\\}", "}")
    s = s.replace("~", "\u00a0")          # non-breaking space → unicode
    s = re.sub(r"\\ ", " ", s)            # backslash-space
    # Triangle marker used as sub-header
    s = re.sub(r"\$\\triangle\$", "▲", s)
    s = re.sub(r"\$\\Delta\$",    "▲", s)
    # Strip remaining LaTeX commands
    s = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", s)  # \cmd{arg} → arg
    s = re.sub(r"\\[a-zA-Z]+\b", "",  s)              # bare \cmd → nothing
    s = re.sub(r"\{([^}]*)\}", r"\1", s)              # leftover { } pairs
    # Remove any remaining stray braces
    s = s.replace("{", "").replace("}", "")
    # Collapse whitespace
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


# ══════════════════════════════════════════════════════════════════════════
# Brace-aware argument reader
# ══════════════════════════════════════════════════════════════════════════

def read_braced_arg(text: str, pos: int):
    """
    Starting at pos (which must be '{'), return (inner_content, pos_after_close).
    Handles nested braces and \\{ / \\} escapes.
    """
    assert text[pos] == "{", f"Expected '{{' at {pos}, got {text[pos]!r}"
    depth = 0
    start = pos + 1
    i = pos
    while i < len(text):
        if text[i] == "\\" and i + 1 < len(text):
            i += 2          # skip escaped char
            continue
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return text[start:i], i + 1
        i += 1
    raise ValueError(f"Unmatched '{{' at position {pos}")


def read_n_args(text: str, pos: int, n: int):
    """
    Read n consecutive {arg} blocks, skipping whitespace between them.
    Returns (list_of_args, pos_after_last_close).
    """
    args = []
    for _ in range(n):
        while pos < len(text) and text[pos] in " \t\n\r":
            pos += 1
        if pos >= len(text) or text[pos] != "{":
            args.append("")
            continue
        arg, pos = read_braced_arg(text, pos)
        args.append(arg)
    return args, pos


# ══════════════════════════════════════════════════════════════════════════
# cv.tex parser
# ══════════════════════════════════════════════════════════════════════════

def parse_cv(tex_path: Path):
    """
    Returns list of (section_title: str, entries: list[dict]).
    Each entry dict has a 'type' key: 'cventry' | 'cvitem' | 'cvitemwithcomment' | 'bibliography'.
    """
    text = strip_latex_comments(tex_path.read_text(encoding="utf-8"))

    # Extract body inside \begin{document}...\end{document}
    m = re.search(r"\\begin\{document\}(.*?)\\end\{document\}", text, re.DOTALL)
    if not m:
        sys.exit("ERROR: could not find \\begin{document}...\\end{document}")
    body = m.group(1)

    sections = []
    current_title   = None
    current_entries = []

    i = 0
    while i < len(body):

        # ── \section{Title} ───────────────────────────────────────────────
        m = re.match(r"\\section\s*\{", body[i:])
        if m:
            if current_title is not None:
                sections.append((current_title, current_entries))
            pos = i + len(m.group(0)) - 1   # position of '{'
            title_raw, end = read_braced_arg(body, pos)
            current_title   = latex_to_md(title_raw)
            current_entries = []
            i = end
            continue

        # ── \cventry{dates}{title}{institution}{location}{grade}{desc} ────
        m = re.match(r"\\cventry\s*\{", body[i:])
        if m:
            pos = i + len(m.group(0)) - 1
            args, end = read_n_args(body, pos, 6)
            dates, title, institution, location, grade, description = args

            # skip pure spacer entries
            if all(a.strip() == "" for a in args):
                i = end
                continue

            entry = {
                "type":        "cventry",
                "dates":       latex_to_md(dates),
                "title":       latex_to_md(title),
                "institution": latex_to_md(institution),
                "location":    latex_to_md(location),
                "grade":       latex_to_md(grade),
                "description": latex_to_md(description),
            }
            current_entries.append(entry)
            i = end
            continue

        # ── \cvitem{key}{value} ───────────────────────────────────────────
        m = re.match(r"\\cvitem\s*\{", body[i:])
        if m:
            pos = i + len(m.group(0)) - 1
            args, end = read_n_args(body, pos, 2)
            key, value = args
            if key.strip() == "" and value.strip() == "":
                i = end
                continue
            current_entries.append({
                "type":  "cvitem",
                "key":   latex_to_md(key),
                "value": latex_to_md(value),
            })
            i = end
            continue

        # ── \cvitemwithcomment{key}{value}{comment} ───────────────────────
        m = re.match(r"\\cvitemwithcomment\s*\{", body[i:])
        if m:
            pos = i + len(m.group(0)) - 1
            args, end = read_n_args(body, pos, 3)
            key, value, comment = args
            current_entries.append({
                "type":    "cvitemwithcomment",
                "key":     latex_to_md(key),
                "value":   latex_to_md(value),
                "comment": latex_to_md(comment),
            })
            i = end
            continue

        # ── \bibliography{file} ───────────────────────────────────────────
        # Treat \bibliography as its own "Publications" section so it doesn't
        # get nested inside whatever section happens to precede it in the .tex.
        m = re.match(r"\\bibliography\s*\{", body[i:])
        if m:
            if current_title is not None:
                sections.append((current_title, current_entries))
            current_title   = "Publications"
            current_entries = []
            pos = i + len(m.group(0)) - 1
            bib_name, end = read_braced_arg(body, pos)
            current_entries.append({"type": "bibliography", "file": bib_name.strip()})
            i = end
            continue

        i += 1

    if current_title is not None:
        sections.append((current_title, current_entries))

    return sections


# ══════════════════════════════════════════════════════════════════════════
# publications.bib parser
# ══════════════════════════════════════════════════════════════════════════

def parse_bib(bib_path: Path):
    """Returns list of field-dicts for each bib entry."""
    text = bib_path.read_text(encoding="utf-8")

    # Strip Jekyll front matter (--- ... ---) if present
    if text.lstrip().startswith("---"):
        end = text.find("---", text.find("---") + 3)
        if end != -1:
            text = text[end + 3:]

    entries = []
    i = 0

    while i < len(text):
        at = text.find("@", i)
        if at == -1:
            break

        m = re.match(r"@(\w+)\s*\{", text[at:])
        if not m:
            i = at + 1
            continue

        entry_type = m.group(1).lower()
        brace_pos  = at + len(m.group(0)) - 1   # position of '{'

        try:
            content, end = read_braced_arg(text, brace_pos)
        except ValueError:
            i = at + 1
            continue

        if entry_type in ("comment", "string", "preamble"):
            i = end
            continue

        comma = content.find(",")
        key         = content[:comma].strip() if comma != -1 else content.strip()
        fields_text = content[comma + 1:] if comma != -1 else ""

        fields = {"type": entry_type, "key": key}

        # Parse field = {value} | "value" | number
        j = 0
        while j < len(fields_text):
            # skip whitespace / commas
            while j < len(fields_text) and fields_text[j] in " \t\n\r,":
                j += 1

            nm = re.match(r"(\w+)\s*=\s*", fields_text[j:])
            if not nm:
                j += 1
                continue

            fname = nm.group(1).lower()
            j    += len(nm.group(0))

            # skip whitespace
            while j < len(fields_text) and fields_text[j] in " \t":
                j += 1

            if j >= len(fields_text):
                break

            if fields_text[j] == "{":
                value, j = read_braced_arg(fields_text, j)
            elif fields_text[j] == '"':
                eq = fields_text.find('"', j + 1)
                value = fields_text[j + 1:eq] if eq != -1 else ""
                j = eq + 1 if eq != -1 else len(fields_text)
            else:
                # bare number or month abbreviation
                end_v = j
                while end_v < len(fields_text) and fields_text[end_v] not in ",}\n":
                    end_v += 1
                value = fields_text[j:end_v].strip()
                j = end_v

            fields[fname] = value

        entries.append(fields)
        i = end

    return entries


# ══════════════════════════════════════════════════════════════════════════
# HTML generation  (news-card design, collapsible sections)
# ══════════════════════════════════════════════════════════════════════════

import html as _html

def h(s: str) -> str:
    """HTML-escape a plain-text string."""
    return _html.escape(str(s), quote=True)


def resolve_link(val: str, base_prefix: str = "") -> str:
    """Return a usable href: absolute URLs pass through, relative ones get base_prefix."""
    if not val:
        return ""
    if val.startswith("http://") or val.startswith("https://"):
        return val
    return base_prefix + val.lstrip("/")


def format_bib_html(e: dict) -> str:
    """Format one bib entry as a compact pub-card HTML block."""
    title    = h(latex_to_md(e.get("title",  "").strip().strip("{}")))
    authors  = h(latex_to_md(e.get("author", "").replace("\n", " ")))
    year     = e.get("year", "")
    etype    = e.get("type", "")
    note     = h(latex_to_md(e.get("note", "")))
    abstract = h(latex_to_md(e.get("abstract", "")))

    if etype == "article":
        venue = h(latex_to_md(e.get("journal", "")))
    elif etype in ("inproceedings", "incollection"):
        venue = h(latex_to_md(e.get("booktitle", "").strip().strip("{}")))
    elif etype in ("phdthesis", "mastersthesis"):
        venue = f"PhD Thesis, {h(latex_to_md(e.get('school', '')))}"
    elif etype == "misc":
        venue = h(latex_to_md(e.get("howpublished", "")))
    else:
        venue = ""

    venue_str = venue
    if year:
        venue_str += f", {year}" if venue_str else year
    if note:
        venue_str += f" <em>({note})</em>"

    # Links
    links_html = ""
    doi = e.get("doi", "")
    if doi:
        links_html += f'<a href="https://doi.org/{h(doi)}" class="pub-link" target="_blank">DOI</a> '
    for field, label in [("pdf","PDF"),("website","Website"),("code","Code"),("slides","Slides")]:
        val = e.get(field, "")
        if not val:
            continue
        if not val.startswith("http"):
            val = "/assets/pdf/" + val.lstrip("/")
        links_html += f'<a href="{h(val)}" class="pub-link" target="_blank">{label}</a> '

    abstract_html = ""
    if abstract:
        abstract_html = (f'<details class="pub-card__details">'
                         f'<summary>Abstract</summary><p>{abstract}</p></details>')

    return (f'<div class="pub-card" style="margin-bottom:0.5rem;">'
            f'<div class="pub-card__body">'
            f'<div class="pub-card__title-row"><h3 class="pub-card__title">{title}</h3></div>'
            f'<div class="pub-card__authors">{authors}</div>'
            f'<div class="pub-card__venue"><em>{venue_str}</em></div>'
            f'<div class="pub-card__links">{links_html}</div>'
            f'{abstract_html}'
            f'</div></div>\n')


# ── CV entry helpers ───────────────────────────────────────────────────────

_ROW  = "padding:0.55rem 0; border-bottom:1px solid rgba(255,255,255,0.05);"
_TTL  = "font-weight:600; font-size:0.88rem; color:rgba(238,238,238,0.9);"
_META = "font-size:0.78rem; color:rgba(238,238,238,0.5); margin-top:0.15rem;"
_DATE = "font-size:0.75rem; color:rgba(238,238,238,0.35); white-space:nowrap; flex-shrink:0;"
_SUM  = ("font-size:0.72rem; color:rgba(238,238,238,0.4); cursor:pointer; "
         "user-select:none; margin-top:0.3rem; display:inline-block;")
_DESC = "font-size:0.8rem; color:rgba(238,238,238,0.65); margin:0.35rem 0 0; line-height:1.6;"


def cventry_html(entry: dict) -> str:
    dates  = h(entry["dates"])
    etitle = entry["title"]
    inst   = h(entry["institution"])
    loc    = h(entry["location"])
    desc   = entry["description"]

    if etitle.startswith("▲"):
        return (f'<div style="margin:0.9rem 0 0.3rem; font-size:0.78rem; font-weight:700; '
                f'color:rgba(238,238,238,0.4); text-transform:uppercase; letter-spacing:0.06em;">'
                f'{h(etitle)}</div>\n')

    meta   = " · ".join(p for p in [inst, loc] if p)
    meta_h = f'<div style="{_META}">{meta}</div>' if meta else ""
    desc_h = ""
    if desc.strip():
        body = "".join(f'<p style="{_DESC}">{h(l.strip())}</p>'
                       for l in desc.split("\n") if l.strip())
        desc_h = f'<details><summary style="{_SUM}">Details</summary>{body}</details>'

    row = (f'<div style="{_ROW}">'
           f'<div style="display:flex;justify-content:space-between;align-items:baseline;gap:0.5rem;flex-wrap:wrap;">'
           f'<span style="{_TTL}">{h(etitle)}</span>'
           f'<span style="{_DATE}">{dates}</span></div>'
           f'{meta_h}{desc_h}</div>')
    return row + "\n"


def cvitem_html(entry: dict) -> str:
    key, val = h(entry["key"]), h(entry["value"])
    if not key and not val:
        return ""
    if key:
        return (f'<div style="{_ROW}">'
                f'<span style="{_TTL}">{key}:</span> '
                f'<span style="font-size:0.82rem;color:rgba(238,238,238,0.7);">{val}</span>'
                f'</div>\n')
    return f'<div style="{_META}padding:0.3rem 0;">{val}</div>\n'


def cvitemwithcomment_html(entry: dict) -> str:
    key, val, cmt = h(entry["key"]), h(entry["value"]), h(entry["comment"])
    right = (f'<span style="color:rgba(238,238,238,0.3);font-size:0.75rem;">{cmt}</span>'
             if cmt else "")
    return (f'<div style="{_ROW}display:flex;justify-content:space-between;">'
            f'<span><span style="{_TTL}">{key}:</span> '
            f'<span style="font-size:0.82rem;color:rgba(238,238,238,0.7);">{val}</span></span>'
            f'{right}</div>\n')


def bib_section_html(bib_entries: list) -> str:
    by_year = defaultdict(list)
    for e in bib_entries:
        by_year[e.get("year", "n.d.")].append(e)
    parts = []
    for year in sorted(by_year.keys(), reverse=True):
        parts.append(
            f'<div style="margin:0.6rem 0 0.3rem;font-size:0.72rem;font-weight:700;'
            f'text-transform:uppercase;letter-spacing:0.08em;color:rgba(238,238,238,0.35);">'
            f'{year}</div>\n')
        for e in by_year[year]:
            parts.append(format_bib_html(e))
    return "\n".join(parts)


def sections_to_html(sections: list, bib_entries: list) -> str:
    parts = []
    for sec_title, entries in sections:
        if not entries:
            continue
        body_parts = []
        for entry in entries:
            etype = entry.get("type")
            if   etype == "cventry":           body_parts.append(cventry_html(entry))
            elif etype == "cvitem":            body_parts.append(cvitem_html(entry))
            elif etype == "cvitemwithcomment": body_parts.append(cvitemwithcomment_html(entry))
            elif etype == "bibliography":      body_parts.append(bib_section_html(bib_entries))
        body = "".join(body_parts).strip()
        if not body:
            continue
        parts.append(
            f'<details class="news-card" style="margin-bottom:0.6rem;">\n'
            f'  <summary class="news-card__header" style="cursor:pointer;list-style:none;'
            f'display:flex;justify-content:space-between;align-items:center;">\n'
            f'    <span class="news-card__title">{h(sec_title)}</span>\n'
            f'  </summary>\n'
            f'  <div class="news-card__body" style="padding-top:0.5rem;">\n'
            f'{body}\n'
            f'  </div>\n'
            f'</details>\n')
    return "\n".join(parts)


def write_cv_md(sections, bib_entries, out_path: Path):
    front_matter = """\
---
layout: page
title: CV
permalink: /cv/
description: Curriculum Vitae
---

<div style="text-align:right; margin-bottom:1.5rem;">
  <a href="/assets/pdf/CV_Behzad.pdf" class="pub-link" target="_blank">⬇&nbsp;Download PDF</a>
</div>

"""
    content = sections_to_html(sections, bib_entries)
    out_path.write_text(front_matter + content, encoding="utf-8")
    print(f"  ✓  Written: {out_path.relative_to(REPO)}")


# ══════════════════════════════════════════════════════════════════════════
# PDF compilation
# ══════════════════════════════════════════════════════════════════════════

def compile_pdf(tex_path: Path, bib_path: Path, out_pdf: Path):
    # Common install locations for BasicTeX / MacTeX on macOS
    _EXTRA_TEX_DIRS = [
        "/Library/TeX/texbin",
        "/usr/local/texlive/2026basic/bin/universal-darwin",
        "/usr/local/texlive/2025basic/bin/universal-darwin",
        "/usr/local/texlive/2024basic/bin/universal-darwin",
        "/usr/local/texlive/2026/bin/universal-darwin",
        "/usr/local/texlive/2025/bin/universal-darwin",
        "/usr/local/texlive/2024/bin/universal-darwin",
    ]

    def _find(cmd):
        found = shutil.which(cmd)
        if found:
            return found
        for d in _EXTRA_TEX_DIRS:
            p = Path(d) / cmd
            if p.exists():
                return str(p)
        return None

    pdflatex = _find("pdflatex")
    bibtex   = _find("bibtex")

    if not pdflatex:
        print("  ✗  pdflatex not found – skipping PDF compilation.")
        print("     Install TeX Live / MiKTeX and make sure pdflatex is on PATH.")
        return False

    with tempfile.TemporaryDirectory(prefix="cv_build_") as tmp:
        tmp = Path(tmp)
        shutil.copy(tex_path, tmp / tex_path.name)
        # Strip Jekyll front matter (--- ---) before handing to LaTeX.
        # cv.tex uses \bibliography{publications}, so always write as publications.bib.
        bib_text = bib_path.read_text(encoding="utf-8")
        if bib_text.lstrip().startswith("---"):
            end = bib_text.find("---", bib_text.find("---") + 3)
            if end != -1:
                bib_text = bib_text[end + 3:]
        (tmp / "publications.bib").write_text(bib_text, encoding="utf-8")
        stem = tex_path.stem

        def run(cmd):
            r = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
            if r.returncode != 0:
                # Print last 30 lines of stdout for debugging
                tail = "\n".join(r.stdout.splitlines()[-30:])
                print(f"\n  ✗  {cmd[0]} returned {r.returncode}:\n{tail}\n")
            return r.returncode == 0

        ok  = run([pdflatex, "-interaction=nonstopmode", stem + ".tex"])
        if bibtex:
            run([bibtex, stem])
        ok &= run([pdflatex, "-interaction=nonstopmode", stem + ".tex"])
        ok &= run([pdflatex, "-interaction=nonstopmode", stem + ".tex"])

        pdf_src = tmp / f"{stem}.pdf"
        if pdf_src.exists():
            out_pdf.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(pdf_src, out_pdf)
            print(f"  ✓  PDF written: {out_pdf.relative_to(REPO)}")
            return True
        else:
            print("  ✗  PDF not produced (check LaTeX errors above).")
            return False


# ══════════════════════════════════════════════════════════════════════════
# Entry point
# ══════════════════════════════════════════════════════════════════════════

def main():
    print("=== CV Render ===\n")

    # 1. Parse LaTeX source
    print("Parsing cv.tex ...")
    sections = parse_cv(CV_TEX)
    print(f"  Found {len(sections)} sections: {[s[0] for s in sections]}")

    # 2. Parse publications from the site bib
    print(f"Parsing {SITE_BIB.name} ...")
    bib = parse_bib(SITE_BIB)
    print(f"  Found {len(bib)} publications")

    # 3. Generate web CV page
    print("\nGenerating _pages/cv.md ...")
    write_cv_md(sections, bib, MD_OUT)

    # 4. Compile PDF (uses site bib, Jekyll front matter stripped automatically)
    print("\nCompiling PDF ...")
    compile_pdf(CV_TEX, SITE_BIB, PDF_OUT)

    print("\n=== Done ===")
    print("Run  bundle exec jekyll serve  to preview the site.")


if __name__ == "__main__":
    main()
