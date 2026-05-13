---
layout: page
title: Dev Resources
permalink: /dev-resources/
description: Frameworks, templates, and interactive widgets for developers.
hide_title: true
---

{% assign framework_posts = site.posts | where_exp: "doc", "doc.project_types contains 'frameworks-templates'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign widget_posts = site.posts | where_exp: "doc", "doc.project_types contains 'web-widgets'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}

{% if framework_posts.size > 0 %}
<details class="project-section" id="frameworks-templates">
  <summary class="project-section__header">
    Frameworks & Templates
    <a class="section-anchor" href="#frameworks-templates" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="row">
      {% for doc in framework_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      <div class="col col-6 col-t-12">{% include display_post_card.html doc=doc %}</div>
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if widget_posts.size > 0 %}
<details class="project-section" id="web-widgets">
  <summary class="project-section__header">
    Web Widgets
    <a class="section-anchor" href="#web-widgets" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="row">
      {% for doc in widget_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      <div class="col col-6 col-t-12">{% include display_post_card.html doc=doc %}</div>
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}
