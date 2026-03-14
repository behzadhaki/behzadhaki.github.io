---
layout: page
permalink: /repositories/
title: Repositories
description: GitHub repositories and activity
---

## GitHub Users

{% if site.data.repositories.github_users %}
<div style="display: flex; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 2rem;">
  {% for user in site.data.repositories.github_users %}
    {% include repository/repo_user.html username=user %}
  {% endfor %}
</div>
{% endif %}

---

## GitHub Repositories

{% if site.data.repositories.github_repos %}
<div style="display: flex; flex-wrap: wrap; gap: 1.5rem;">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo.html repository=repo %}
  {% endfor %}
</div>
{% endif %}
