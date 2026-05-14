---
layout: page
title: "Installations & Performances"
permalink: /installations-performances/
hide_title: true
---

{% assign posts = site.posts | where_exp: "doc", "doc.project_types contains 'installations-performances'" | sort: "date" | reverse %}
<div class="works-card-grid">
{% for doc in posts %}{% if doc.hidden %}{% continue %}{% endif %}
{% include display_post_card.html doc=doc %}
{% endfor %}
</div>
