#!/usr/bin/env python3
"""
Ensures every Landing.md in _posts/projects/ has a permalink.
- If permalink already exists: leave it untouched.
- If missing: inject /projects/{folder_name}/ (lowercased, slugified).
"""

import re
import sys
from pathlib import Path

POSTS_ROOT = Path(__file__).parent.parent / "_posts" / "projects"


def slugify(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return name.strip("-")


def process(path: Path, dry_run: bool) -> str | None:
    """Return the injected permalink string, or None if skipped."""
    text = path.read_text(encoding="utf-8")

    # Must have frontmatter
    if not text.startswith("---"):
        print(f"  SKIP (no frontmatter): {path}")
        return None

    # Find the closing --- of the frontmatter
    end = text.index("---", 3)
    front = text[3:end]

    if re.search(r"^permalink\s*:", front, re.MULTILINE):
        print(f"  OK (has permalink):    {path.parent.name}")
        return None

    folder = path.parent.name
    permalink = f"/projects/{slugify(folder)}/"

    # Insert permalink before the closing ---
    new_front = front.rstrip() + f"\npermalink: {permalink}\n"
    new_text = "---" + new_front + "---" + text[end + 3:]

    if dry_run:
        print(f"  DRY-RUN: would add    {permalink}  →  {path.parent.name}")
    else:
        path.write_text(new_text, encoding="utf-8")
        print(f"  ADDED:                {permalink}  →  {path.parent.name}")

    return permalink


def main():
    dry_run = "--dry-run" in sys.argv
    if dry_run:
        print("Dry-run mode — no files will be modified.\n")

    landing_files = sorted(POSTS_ROOT.rglob("*Landing*.md"))
    if not landing_files:
        print(f"No Landing.md files found under {POSTS_ROOT}")
        sys.exit(1)

    for path in landing_files:
        process(path, dry_run)


if __name__ == "__main__":
    main()
