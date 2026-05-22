---
layout: page
title: "Showcases"
permalink: /showcases/
hide_title: true
---

{% assign all_showcases      = site.posts | where_exp: "doc", "doc.project_types contains 'showcases'" | where_exp: "doc", "doc.hidden != true" | sort: "date" | reverse %}
{% assign installation_posts = all_showcases | where: "showcase_type", "installation" %}
{% assign performance_posts  = all_showcases | where: "showcase_type", "live-performance" %}
{% assign demo_posts         = all_showcases | where: "showcase_type", "demo" %}

<div class="works-filter" id="showcases-filter">
  <button class="works-filter__btn is-active" data-filter="all">All</button>
  {% if installation_posts.size > 0 %}<button class="works-filter__btn" data-filter="installation">Installation</button>{% endif %}
  {% if performance_posts.size > 0 %}<button class="works-filter__btn" data-filter="live-performance">Live Performance</button>{% endif %}
  {% if demo_posts.size > 0 %}<button class="works-filter__btn" data-filter="demo">Demo</button>{% endif %}
</div>

<div class="works-card-grid" id="showcases-grid">
{% for doc in all_showcases %}
{% include display_post_card.html doc=doc %}
{% endfor %}
</div>

<script>
(function () {
  var btns  = Array.from(document.querySelectorAll("#showcases-filter .works-filter__btn"));
  var cards = Array.from(document.querySelectorAll("#showcases-grid .work-card"));

  function applyFilter(filter) {
    btns.forEach(function (b) { b.classList.toggle("is-active", b.dataset.filter === filter); });
    cards.forEach(function (card) {
      var show = filter === "all" || card.dataset.showcaseType === filter;
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
}());
</script>
