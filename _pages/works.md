---
layout: page
title: Works
permalink: /works/
description: Software, hardware, and datasets I have developed.
hide_title: true
---

{% assign max_posts          = site.posts | where_exp: "doc", "doc.project_types contains 'max'"                        | where_exp: "doc", "doc.hidden != true" %}
{% assign pd_posts           = site.posts | where_exp: "doc", "doc.project_types contains 'pd'"                         | where_exp: "doc", "doc.hidden != true" %}
{% assign plugin_posts       = site.posts | where_exp: "doc", "doc.project_types contains 'plugins'"                    | where_exp: "doc", "doc.hidden != true" %}
{% assign web_posts          = site.posts | where_exp: "doc", "doc.project_types contains 'web'"                        | where_exp: "doc", "doc.hidden != true" %}
{% assign hardware_posts     = site.posts | where_exp: "doc", "doc.project_types contains 'hardware'"                   | where_exp: "doc", "doc.hidden != true" %}
{% assign dataset_posts      = site.posts | where_exp: "doc", "doc.project_types contains 'datasets'"             | where_exp: "doc", "doc.hidden != true" %}
{% assign framework_posts    = site.posts | where_exp: "doc", "doc.project_types contains 'frameworks'" | where_exp: "doc", "doc.hidden != true" %}
{% assign template_posts     = site.posts | where_exp: "doc", "doc.project_types contains 'templates'"  | where_exp: "doc", "doc.hidden != true" %}
{% assign webwidget_posts    = site.posts | where_exp: "doc", "doc.project_types contains 'web-widgets'" | where_exp: "doc", "doc.hidden != true" %}

{% assign all_works = "" | split: "" | concat: max_posts | concat: pd_posts | concat: plugin_posts | concat: web_posts | concat: hardware_posts | concat: dataset_posts | concat: framework_posts | concat: template_posts | concat: webwidget_posts | uniq | sort: "date" | reverse %}

<div class="works-filter" id="works-filter">
  <button class="works-filter__btn is-active" data-filter="all">All</button>
  {% if max_posts.size > 0 %}<button class="works-filter__btn" data-filter="max">MAX / M4L</button>{% endif %}
  {% if pd_posts.size > 0 %}<button class="works-filter__btn" data-filter="pd">Pure Data</button>{% endif %}
  {% if plugin_posts.size > 0 %}<button class="works-filter__btn" data-filter="plugins">Plugins</button>{% endif %}
  {% if web_posts.size > 0 %}<button class="works-filter__btn" data-filter="web">Web</button>{% endif %}
  {% if hardware_posts.size > 0 %}<button class="works-filter__btn" data-filter="hardware">Hardware</button>{% endif %}
  {% if dataset_posts.size > 0 %}<button class="works-filter__btn" data-filter="datasets">Datasets</button>{% endif %}
  {% if framework_posts.size > 0 %}<button class="works-filter__btn" data-filter="frameworks">Frameworks</button>{% endif %}
  {% if template_posts.size > 0 %}<button class="works-filter__btn" data-filter="templates">Templates</button>{% endif %}
  {% if webwidget_posts.size > 0 %}<button class="works-filter__btn" data-filter="web-widgets">Web Widgets</button>{% endif %}
</div>

<div class="works-card-grid" id="works-grid">
  {% for doc in all_works %}
  {% include display_post_card.html doc=doc %}
  {% endfor %}
</div>

<script>
(function () {
  var btns  = Array.from(document.querySelectorAll("#works-filter .works-filter__btn"));
  var cards = Array.from(document.querySelectorAll("#works-grid .work-card"));

  function applyFilter(filter) {
    btns.forEach(function (b) { b.classList.toggle("is-active", b.dataset.filter === filter); });
    cards.forEach(function (card) {
      var types = (card.dataset.types || "").split(" ");
      var show  = filter === "all" || types.indexOf(filter) !== -1;
      card.classList.toggle("work-card--hidden", !show);
    });
  }

  btns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var filter = this.dataset.filter;
      history.replaceState(null, "", filter === "all" ? location.pathname : "#" + filter);
      applyFilter(filter);
    });
  });

  function applyFromHash() {
    var hash = location.hash.slice(1);
    var matched = btns.find(function (b) { return b.dataset.filter === hash; });
    applyFilter(matched ? hash : "all");
  }

  window.addEventListener("hashchange", applyFromHash);
  applyFromHash();
})();
</script>
