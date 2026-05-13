---
layout: page
title: "Works — Datasets"
permalink: /works/datasets/
hide_title: true
---

{% assign posts = site.posts | where_exp: "doc", "doc.project_types contains 'datasets'" | sort: "date" | reverse %}
<div class="works-card-grid">
{% for doc in posts %}{% if doc.hidden %}{% continue %}{% endif %}
{% include display_post_card.html doc=doc %}
{% endfor %}
</div>
