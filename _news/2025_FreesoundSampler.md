---
layout: post
title: "A new side project I've been working on: FreesoundRack"
date: 2025-11-01 16:11:00-0400
inline: false
---

I've been working on a new fun side project called FreesoundRack. 
It's a sampler plugin that allows you to easily load and play sounds from Freesound.org.
The idea is to be able to quickly curate racks of sounds from Freesound and use them in your music production workflow.

The plugin is still in early development, but for those interested, an early version is available here:

{% assign project = site.posts | where: "title", "Freesound Rack Plugin" | first %}
{% if project %}
  {% include display_post_card.html doc=project %}
{% endif %}
