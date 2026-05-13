---
layout: page
title: Works
permalink: /works/
description: Software, hardware, and datasets I have developed.
hide_title: true
---

{% assign max_posts = site.posts | where_exp: "doc", "doc.project_types contains 'max'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign pd_posts = site.posts | where_exp: "doc", "doc.project_types contains 'pd'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign plugin_posts = site.posts | where_exp: "doc", "doc.project_types contains 'plugins'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign web_posts = site.posts | where_exp: "doc", "doc.project_types contains 'web'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign hardware_posts = site.posts | where_exp: "doc", "doc.project_types contains 'hardware'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign installation_posts = site.posts | where_exp: "doc", "doc.project_types contains 'installations-performances'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign dataset_posts = site.posts | where_exp: "doc", "doc.project_types contains 'datasets'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}

{% if max_posts.size > 0 %}
<details class="project-section" id="max">
  <summary class="project-section__header">
    MAX / M4L
    <a class="section-anchor" href="#max" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in max_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if pd_posts.size > 0 %}
<details class="project-section" id="pd">
  <summary class="project-section__header">
    Pure Data
    <a class="section-anchor" href="#pd" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in pd_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if plugin_posts.size > 0 %}
<details class="project-section" id="plugins">
  <summary class="project-section__header">
    Plugins
    <a class="section-anchor" href="#plugins" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in plugin_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if web_posts.size > 0 %}
<details class="project-section" id="web">
  <summary class="project-section__header">
    Web
    <a class="section-anchor" href="#web" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in web_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if hardware_posts.size > 0 %}
<details class="project-section" id="hardware">
  <summary class="project-section__header">
    Hardware
    <a class="section-anchor" href="#hardware" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in hardware_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if installation_posts.size > 0 %}
<details class="project-section" id="installations-performances">
  <summary class="project-section__header">
    Installations & Performances
    <a class="section-anchor" href="#installations-performances" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in installation_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}

{% if dataset_posts.size > 0 %}
<details class="project-section" id="datasets">
  <summary class="project-section__header">
    Datasets
    <a class="section-anchor" href="#datasets" title="Copy link to this section" aria-label="Copy link to this section"><i class="fa-solid fa-link"></i></a>
  </summary>
  <div class="project-section__body">
    <div class="works-card-grid">
      {% for doc in dataset_posts %}{% if doc.hidden %}{% continue %}{% endif %}
      {% include display_post_card.html doc=doc %}
      {% endfor %}
    </div>
  </div>
</details>
{% endif %}
