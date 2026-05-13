---
layout: page
title: "Works — Plugins"
permalink: /works/plugins/
hide_title: true
---

{% assign posts = site.posts | where_exp: "doc", "doc.project_types contains 'plugins'" | sort: "date" | reverse %}
<div class="works-card-grid">
{% for doc in posts %}{% if doc.hidden %}{% continue %}{% endif %}
{% include display_post_card.html doc=doc %}
{% endfor %}
</div>
