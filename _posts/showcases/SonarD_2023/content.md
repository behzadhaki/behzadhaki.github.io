
## Overview

We had a demo booth at the modular project area of the Sonar+D 2023 festival in Barcelona, where we showcased the GrooveTransformer Eurorack module, a generative sequencer developed by Nicholas Evans and me.


## Technical Resources

The GrooveTransformer is a generative sequencer developed by Nicholas Evans and me. 

The GrooveTransformer is available openly as a plugin. Read more about the software version here:

<div class="works-card-grid">
  {% assign project = site.posts | where: "title", "GrooveTransformer VST" | first %}
  {% if project %}{% include display_post_card.html doc=project %}{% endif %}
</div>



A Eurorack hardware version of it has also been developed by us, which was used in this showcase. Read more about the hardware version here:

<div class="works-card-grid">
  {% assign project = site.posts | where: "title", "GrooveTransformer Eurorack" | first %}
  {% if project %}{% include display_post_card.html doc=project %}{% endif %}
</div>

## Publications

We've had a few publications involving the eurorack module. You can find them here:

<div class="publications">
  {% bibliography -f papers -q @*[key=Haki2024GrooveTransformer] %}
  {% bibliography -f papers -q @*[key=kotowski_2025_16946740] %}
</div>
