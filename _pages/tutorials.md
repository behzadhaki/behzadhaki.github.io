---
layout: page
title: Tutorials
permalink: /tutorials/
hide_title: true
description: Step-by-step guides for developing audio applications with JUCE, Freesound, and related tools.
---

{% assign tutorial_posts = site.posts | sort: "date" | reverse %}

<div class="row">
{% for doc in tutorial_posts %}
{% if doc.in_collections contains 'development-tools' %}
<div class="col col-6 col-t-12">
{% include display_post_card.html doc=doc %}
</div>
{% endif %}
{% endfor %}
</div>
