---
layout: page
title: Dev Resources
permalink: /dev-resources/
description: Frameworks, templates, and interactive widgets for developers.
hide_title: true
---

{% assign framework_posts = site.posts | where_exp: "doc", "doc.project_types contains 'frameworks-templates'" | where_exp: "doc", "doc.hidden != true" %}
{% assign widget_posts    = site.posts | where_exp: "doc", "doc.project_types contains 'web-widgets'"          | where_exp: "doc", "doc.hidden != true" %}

{% assign all_devres = "" | split: "" | concat: framework_posts | concat: widget_posts | uniq | sort: "date" | reverse %}

<div class="works-filter" id="devres-filter">
  <button class="works-filter__btn is-active" data-filter="all">All</button>
  {% if framework_posts.size > 0 %}<button class="works-filter__btn" data-filter="frameworks-templates">Frameworks & Templates</button>{% endif %}
  {% if widget_posts.size > 0 %}<button class="works-filter__btn" data-filter="web-widgets">Web Widgets</button>{% endif %}
</div>

<div class="works-card-grid" id="devres-grid">
  {% for doc in all_devres %}
  {% include display_post_card.html doc=doc %}
  {% endfor %}
</div>

<script>
(function () {
  var btns  = Array.from(document.querySelectorAll("#devres-filter .works-filter__btn"));
  var cards = Array.from(document.querySelectorAll("#devres-grid .work-card"));
  var active = "all";

  btns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      active = this.dataset.filter;
      btns.forEach(function (b) { b.classList.toggle("is-active", b.dataset.filter === active); });
      cards.forEach(function (card) {
        var types = (card.dataset.types || "").split(" ");
        var show  = active === "all" || types.indexOf(active) !== -1;
        card.classList.toggle("work-card--hidden", !show);
      });
    });
  });
})();
</script>
