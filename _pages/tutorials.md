---
layout: page
title: Tutorials
permalink: /tutorials/
hide_title: true
description: Step-by-step guides for developing audio applications with JUCE, Freesound, and related tools.
---

{% assign tutorial_posts = site.posts | where_exp: "doc", "doc.project_types contains 'tutorials'" | sort: "date" | reverse %}

<div class="row">
{% for doc in tutorial_posts %}{% if doc.hidden %}{% continue %}{% endif %}
<div class="col col-6 col-t-12">
{% include display_post_card.html doc=doc %}
</div>
{% endfor %}
</div>
