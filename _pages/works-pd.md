---
layout: page
title: "Works — Pure Data"
permalink: /works/pd/
hide_title: true
---

{% assign posts = site.posts | where_exp: "doc", "doc.project_types contains 'pd'" | sort: "date" | reverse %}
<div class="works-card-grid">
{% for doc in posts %}{% if doc.hidden %}{% continue %}{% endif %}
{% include display_post_card.html doc=doc %}
{% endfor %}
</div>
