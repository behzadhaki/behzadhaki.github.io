{% comment %}
Usage:
{% include safe-include.md file="overview.md" %}
{% endcomment %}

{% capture file_content %}
  {% include_relative {{ include.file }} %}
{% endcapture %}

{% if file_content contains "Liquid error" %}
  <p style="color: red;"><strong>Missing file:</strong> <code>{{ include.file }}</code> not found next to <code>{{ page.path }}</code>.</p>
{% elsif file_content == "" %}
  <p><em>Content not provided by author(s).</em></p>
{% else %}
  {{ file_content | markdownify }}
{% endif %}
