The website here is based on Norlin (a paid template). You should not clone this repository.

To create a similar website, you can purchase the Norlin template from https://jekyllthemes.io/theme/norlin-dark-blog-jekyll-theme and follow the instructions provided with the template to set up your own website.



---- 

install the dependencies:

```terminal
bundle install
```

Running the website locally:

```terminal
python3 scripts/run_all.py && bundle exec jekyll serve --livereload
```

Note the cv is auto-generated using the latex source file located at `assets/cv_latex/cv.tex`.
The bibliography in the cv is generated from '_bibliography/papers.bib' file.

## Adding / editing posts

Run the post builder tool:

```terminal
python3 _tools/dev-server.py
```

Then open: http://localhost:4099/_tools/new-post-builder.html

## Inline buttons in post body

Two includes let you embed styled buttons anywhere in a post's Markdown body.

### Single button

```liquid
{% include btn.html type="web" label="Demo" url="https://..." %}
```

### Row of buttons (up to 4)

```liquid
{% include btn-row.html
   type1="github" label1="Code"  url1="https://github.com/..."
   type2="paper"  label2="Paper" url2="https://arxiv.org/..."
   type3="web"    label3="Demo"  url3="https://..." %}
```

### Available types

| type | colour | icon |
|---|---|---|
| `web` | blue | globe |
| `docs` | blue | book |
| `paper` | blue | file |
| `github` | green | GitHub mark |
| `issues` | green | GitHub mark |
| `download` | steel blue | download arrow |
| `mac-arm` | steel blue | Apple |
| `mac-intel` | steel blue | Apple |
| `win` | steel blue | Windows |
| `linux` | steel blue | Linux |
| `license` | muted | download arrow |
| `cite` | muted | download arrow |
| `email` | muted | envelope |
| `unavailable` | greyed out | — |

## Embedding post cards in post body

Use `display_post_card.html` to embed a card linking to another post. Wrap it in `works-card-grid` so the card is sized consistently with the works page (max 220px per card, auto-filling columns for multiple cards).

### Single card

```liquid
<div class="works-card-grid">
  {% assign project = site.posts | where: "title", "Exact Post Title Here" | first %}
  {% if project %}{% include display_post_card.html doc=project %}{% endif %}
</div>
```

### Multiple cards side-by-side

```liquid
<div class="works-card-grid">
  {% assign p1 = site.posts | where: "title", "First Post Title" | first %}
  {% assign p2 = site.posts | where: "title", "Second Post Title" | first %}
  {% if p1 %}{% include display_post_card.html doc=p1 %}{% endif %}
  {% if p2 %}{% include display_post_card.html doc=p2 %}{% endif %}
</div>
```

The grid handles sizing automatically — identical to the works page. Without the `works-card-grid` wrapper the card stretches to fill the full post content width.

## Embedding a publication or reference card

### Bib files

| File | Contents |
|---|---|
| `_bibliography/papers.bib` | Your own publications |
| `_bibliography/refs.bib` | External references / citations |

### Single entry by key

Wrap in `project-pubs` for a single-column card consistent with how references appear inside posts:

```liquid
<div class="project-pubs" style="max-width: 600px;">
  {% bibliography -f papers -q @*[key=YOUR_BIBTEX_KEY] %}
</div>
```

Use `-f refs` instead of `-f papers` when citing an external reference.

### Two-column grid (multiple entries)

Use the `publications` wrapper for a two-column card grid, consistent with the publications page:

```liquid
<div class="publications">
  {% bibliography -f papers -q @*[key=KEY_ONE] %}
  {% bibliography -f papers -q @*[key=KEY_TWO] %}
</div>
```

Or filter by year:

```liquid
<div class="publications">
  {% bibliography -f papers -q @*[year=2024] %}
</div>
```

### Finding a key

Open the relevant `.bib` file and look for the `@article{KEY,` / `@inproceedings{KEY,` identifier — that is the value to pass to `key=`.

### Bib fields that affect rendering

These custom fields in `papers.bib` entries conditionally change what appears on the web CV, the publications page, or the PDF CV.

| Field | Value | Effect |
|---|---|---|
| `hide` | `{true}` | Entry is **excluded from the PDF CV**. Also excluded from the web CV if `note = {Under review}` is set (the web CV already skips "under review" entries independently). |
| `note` | `{Under review}` | Entry is **excluded from the web CV** (`_pages/cv.md`). Still appears on the publications page. Combine with `hide = {true}` to also drop it from the PDF. |
| `preview` | `{filename.png}` | Thumbnail shown on the **publications page** card. Image must be in `assets/img/publication_preview/`. Accepts a full URL too. |
| `abbr` | `{NIME}` | Short venue badge rendered next to the title on the **publications page** card. |
| `bibtex_show` | `{true}` | Adds a collapsible **BibTeX** block to the publications page card. The `filtered_bibtex_keywords` list in `_config.yml` controls which custom fields are stripped before display. |

Link fields below conditionally show a button on the **publications page** card and on the **web CV**. Relative values are resolved under `assets/pdf/`; absolute URLs pass through unchanged.

| Field | Button label |
|---|---|
| `pdf` | PDF |
| `arxiv` | arXiv (value is the arXiv ID, e.g. `2309.00001`) |
| `website` | Website |
| `code` | Code |
| `slides` | Slides |
| `poster` | Poster |
| `supp` | Supp |
| `blog` | Blog |
| `html` | HTML |