---
layout: page
title: News
permalink: /news/
hide_title: true
description: Latest news and updates.
---

{% assign news_items = site.news | sort: "date" | reverse %}

<div class="news-list">
  {% for item in news_items %}
  <div class="news-card">
    <div class="news-card__header">
      <time class="news-card__date" datetime="{{ item.date | date_to_xmlschema }}">
        {{ item.date | date: "%b %-d, %Y" }}
      </time>
      <span class="news-card__title">{{ item.title }}</span>
    </div>
    <div class="news-card__body">
      {{ item.content }}
    </div>
  </div>
  {% endfor %}
</div>
