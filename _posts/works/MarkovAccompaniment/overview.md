
## Overview

Back in November 2024, we had the opportunity to participate in a concert series at Palau Güell. These series, called Organic, were to showcase the main organ fixture of the venue, a large pipe organ designed specifically for the space.

<img src="/assets/works/MarkovAccompaniment/GuellImage3.jpeg" alt="Thumbnail" width="45%">

For this performance, we had access to the main organ, as well as a couple of portable organs (see image below).

<img src="/assets/works/MarkovAccompaniment/Venue2.png" alt="Thumbnail" width="30%">

The concept for the performance was to us a setup in which Raul Refree would perform on the main organ, and the system would generate accompaniments in real-time, played by the portable organs.

The idea was to explore whether and how we could use our prior generative system, which were mainly focused on rhythm, to generate harmonic content for the organ. As such, we developed the system shown below, in which GrooveTransformer is used to generate rhythmic content and a Markov-model is used to generate the harmonic content.

<img src="/assets/works/MarkovAccompaniment/AccompDemo.png" alt="Thumbnail" style="max-width:600px; width:100%">

While the system was originally designed to work with the pipe organ, it can be adapted to work with any pitched instrument, digital or acoustic, that can be controlled via MIDI.