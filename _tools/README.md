# _tools

Developer utilities for the site. These are **not part of the Jekyll build** — they're standalone tools you run locally.

---

## new-post-builder.html

An interactive browser-based wizard for scaffolding new posts.

### Usage

Open a terminal in the **repo root** and start a local HTTP server:

```bash
python3 -m http.server 4099
```

Then open in your browser:

```
http://localhost:4099/_tools/new-post-builder.html
```

> **Do not open the file directly** (`file://…`). It must be served over HTTP so it can fetch the bibliography files from the repo.

### What it does

- Generates a correctly structured `Landing.md` front matter for Works, Tutorials, and Installations/Performances posts
- Creates stub files for each tab (overview, demo, documentation, etc.)
- Creates the `assets/works/<Folder>/` placeholder directory
- Loads available papers from `_bibliography/papers.bib` and `_bibliography/refs.bib` for citation selection
- Lets you add new BibTeX entries inline (they get appended to the correct `.bib` file on write)

### Output options

| Button | What it does |
|---|---|
| **Download ZIP** | Packages all generated files into a `.zip` — works in any browser |
| **Write to Disk** | Writes files directly into the repo using the File System Access API — requires Chrome or Edge (Brave may block it) |

### Notes

- The header shows **📚 N papers** when bib files load successfully. Click it to reload.
- Tags, tabs, link types, and project categories are all editable inline.
- For Works posts that also appear as Installations/Performances, select the "Installation/Performance" category and optionally pick a Works sub-type in the "Also appears in Works as" dropdown.
