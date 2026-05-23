

## Overview

Centre de Cultura Contemporània de Barcelona (CCCB) hosted a six-month long exhibition on Artificial Intelligence:

{% include btn.html type="web" label="More about the program" url="https://www.cccb.org/en/w/exhibitions/ai-artificial-intelligence" %}
<br>

For this exhibition, we prepared an interactive installation in which the public could interact with some of the latest rhythm generation models we had developed. 

The main idea for the installation was to provide a MIDI Bongo interface to allow users to record rhythmic loops, using which the system would generate accompanying drum patterns. 

As a secondary objective of the installation, we crowdsourced a dataset of rhythmic improvisations from various expertise levels. 

To read more about the dataset, read the following post:

<div class="works-card-grid">
  {% assign project = site.posts | where: "title", "El Bongosero" | first %}
  {% if project %}{% include display_post_card.html doc=project %}{% endif %}
</div>
<br>

We have also written a paper going into more details about the installation and the dataset, which you can read here:

<div class="publications">
  {% bibliography -f papers -q @*[key=Haki2024ELBNG] %}
</div>


