---
layout: page
title: Projects
permalink: /projects/
description: Software tools, hardware devices, and datasets I have developed.
hide_title: true
---

<!-- Projects page: lists all posts from _posts/projects/ -->
{% assign all_projects = site.posts | sort: "date" | reverse %}

<div class="row">
{% for doc in all_projects %}
<div class="col col-6 col-t-12">
{% include display_post_card.html doc=doc %}
</div>
{% endfor %}
</div>
