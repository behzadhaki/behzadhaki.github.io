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