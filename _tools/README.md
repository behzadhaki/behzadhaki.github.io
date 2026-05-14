# _tools

Developer utilities for the site. These are **not part of the Jekyll build** — they're standalone tools you run locally.

---

## new-post-builder.html

An interactive browser-based wizard for scaffolding new posts.

### Usage

Run the companion dev server from the **repo root**:

```bash
python3 _tools/dev-server.py
```

Then open in your browser (works in Brave, Chrome, Safari, Firefox):

```
http://localhost:4099/_tools/new-post-builder.html
```

> **Do not open the file directly** (`file://…`). It must be served over HTTP so it can fetch the bibliography files and write files back to the repo.

### What it does

- Generates a correctly structured `Landing.md` front matter for Works, Tutorials, and Installations/Performances posts
- Creates stub files for each tab (overview, demo, documentation, etc.)
- Creates the `assets/works/<Folder>/` or `assets/tutorials/<Folder>/` placeholder directory
- Loads available papers from `_bibliography/papers.bib` and `_bibliography/refs.bib` for citation selection
- Lets you add new BibTeX entries inline (they get appended to the correct `.bib` file on write)
- Upload a hero image — included in ZIP or written directly to the correct assets folder

### Output options

| Button | What it does |
|---|---|
| **Download ZIP** | Packages all generated files into a `.zip` — works in any browser, even without the dev server |
| **Write to Disk** | Writes files directly into the repo via `dev-server.py` (all browsers) or File System Access API (Chrome/Edge fallback) |

### Load & edit existing posts

Click **📂 Load post** and pick any `Landing.md` to pre-fill the form. A banner appears with two modes:

| Mode | Behaviour |
|---|---|
| **⧉ Duplicate** | Change the folder/title → writes to a new location, original untouched |
| **✎ Rename** | Resets folder to original → overwrites files in place |

### Notes

- The header shows **📚 N papers** when bib files load successfully. Click it to reload.
- Tags, tabs, link types, and project categories are all editable inline.
- For Works posts that also appear as Installations/Performances, select the "Installation/Performance" category and optionally pick a Works sub-type in the "Also appears in Works as" dropdown.
- Tutorials use `assets/tutorials/<Folder>/`; Works and Installations use `assets/works/<Folder>/`.

### dev-server.py

A minimal HTTP server that:
- Serves the entire repo over HTTP on port 4099
- Accepts `POST /write-files` requests from the browser tool to write files to disk

This replaces `python3 -m http.server` and is required for **Write to Disk** to work in Brave or any browser that blocks the File System Access API.
