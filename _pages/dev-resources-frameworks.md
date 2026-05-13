---
layout: page
title: "Dev Resources — Frameworks & Templates"
permalink: /dev-resources/frameworks-templates/
hide_title: true
---

{% assign posts = site.posts | where_exp: "doc", "doc.project_types contains 'frameworks-templates'" | sort: "date" | reverse %}
<div class="row">
{% for doc in posts %}{% if doc.hidden %}{% continue %}{% endif %}
<div class="col col-6 col-t-12">{% include display_post_card.html doc=doc %}</div>
{% endfor %}
</div>
