

## Overview

On 29 February 2024, Raül Refree performed a duet with the GrooveTransformer at the Centre de Cultura Contemporània de Barcelona (CCCB), as part of the programme accompanying the CCCB's exhibition *AI: Artificial Intelligence*.

The GrooveTransformer listens to the rhythmic information of a human performer and accompanies them in real time. Although it is based on neural networks, it was designed to be light enough to run on any laptop. Raül Refree and we spent months working together to adapt the system to his playing. The event was conceived as an open rehearsal and marked the public debut of the GrooveTransformer, giving the audience a first look at this evolving collaboration.

{% include btn.html type="web" label="More about the event" url="https://www.cccb.org/en/w/activities/raul-refree-groove-transformer" %}

<br>

<video controls preload="metadata" style="display:block; width:auto; max-width:100%; max-height:240px; margin:1rem 0;">
  <source src="{{ '/assets/showcases/CCCB_AI_Exhibition/VID-20240407-WA0008.mp4' | relative_url }}" type="video/mp4">
  Your browser does not support the video tag.
</video>

<video controls preload="metadata" style="display:block; width:auto; max-width:100%; max-height:420px; margin:1rem 0;">
  <source src="{{ '/assets/showcases/CCCB_AI_Exhibition/Promo%20ENG.mp4' | relative_url }}" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Technical Resources

The GrooveTransformer is a generative sequencer developed by Nicholas Evans and me. This performance was the first showcase in which the GrooveTransformer plugin was used. Read more about the plugin here:

<div class="works-card-grid">
  {% assign project = site.posts | where: "title", "GrooveTransformer VST" | first %}
  {% if project %}{% include display_post_card.html doc=project %}{% endif %}
</div>

## Publications

<div class="publications">
  {% bibliography -f papers -q @*[key=Haki2024GrooveTransformer] %}
</div>
