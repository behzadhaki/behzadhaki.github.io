---
layout: page
title: Tutorials
permalink: /tutorials/
hide_title: true
description: Step-by-step guides for developing audio applications with JUCE, Freesound, and related tools.
---

{% assign tutorial_posts = site.posts | where_exp: "doc", "doc.project_types contains 'tutorials'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}

<div class="works-card-grid">
{% for doc in tutorial_posts %}{% if doc.hidden %}{% continue %}{% endif %}
{% include display_post_card.html doc=doc %}
{% endfor %}
</div>
