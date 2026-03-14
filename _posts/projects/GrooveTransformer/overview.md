
# What is the GrooveTransformer?

At it's core, `GrooveTransformer` is
 
    - a hybrid between a drum sequencer and an accompaniment generator, 
    - designed to be used for real-time live improvisation.

In other words, 
    
    the plugin is a sequencer that generates and playbacks drum loops in real-time,
    using a combination of "programmed" drum patterns and also an incoming rhythmic pattern!

# Story Behind the GrooveTransformer

The GrooveTransformer is very much inspired by the idea of rhythm spaces, that is, the idea of a space in which each point corresponds to a unique rhythm.

The most influential work for us was the [Mutables Instruments' Grids](https://pichenettes.github.io/mutable-instruments-documentation/modules/grids/) module.

This module is a drum sequencer that generates drum patterns in real-time, without requiring the user to program the patterns.

Instead, the module allows the user to navigate a 2D space of rhythms, where each point corresponds to a unique rhythm.

We wanted to take this idea further and create a plugin that allows the user to navigate a custom space, and also, allow the user to "program" the sequencer by specifying the rhythmic "feel" of the drum loop, rather than the exact pattern.

The last idea we had was to utilize rule based algorithms to allow for automatic navigation of the space (if the user desires). 

These considerations would allow us to develop a system that would operate in a variety of ways:

    - As a drum sequencer
    - As an accompaniment generator
    - Or as a hybrid of the two!

We speculated that such a system would afford the user the liberty of deciding where and how the system should be used!

# How does it work?

At the core of the plugin is a small generative neural network that is trained to convert a given rhythmic loop into a drum loop.
Here by rhythmic loop we mean a pitch-agnostic sequence of note-on events, with exact timing and velocity.

Throughout the training process, the selected model attempts to create an abstract space in which each point (or rather region) corresponds to a unique pattern.

GrooveTransformer leverages this latent space to generate new drum loops in real-time.

Specifically, the plugin uses a "triangular" sub-space bounded by three rhythmic ideas:

    - Two of which are user-defined
    - The third is a rhythmic pattern received in real-time.

The plugin then generates drum loops that are dynamically varying within this space.



Let's take closer look at the concept behind the plugin!

## Generative Model

For the GrooveTransformer, we trained a generative neural network that would be able to expand a rhythmic pattern into a 9-voice drum loop.

Rhythmic patterns are in this case represented as a 1D sequence with micro-timing and velocity. That is, we specify on which steps (16th note grid) we want a drum hit, and also how hard the hit should be, and how much it should be offset from the grid.

<img src="/assets/ready-to-use-apps/GrooveTransformer/Groove2Drum.png" alt="Thumbnail" width="50%">



The specific architecture of the neural network is not important for this discussion. What is important though is that beyond  _**<u>converting</u>**_ a rhythmic pattern into a drum loop, the network can also:

1. _**<u>randomly generate</u>**_ new drum loops without any rhythmic input, 
2. _**<u>interpolate</u>**_ between two given drum loops!

<img src="/assets/ready-to-use-apps/GrooveTransformer/model_functionalities.png" alt="Thumbnail" width="50%">

With these capabilities in mind, we can now consider how the plugin operates.


## Exploiting Model Capabilities

### Sequencing between Two Patterns

For the sake of simplicity, let's consider we have two drum loops, `A` and `B`, and we want to generate a new pattern that is a mix of the two. In this case, we can use a slider to specify the degree to which the new pattern should resemble `A` or `B`.

In this case, patterns `A` and `B` can be programmed by the user utilizing a rhythmic seed, or they can be obtained by randomization.

Interpolating between these two patterns, allows for a smooth transition between them, hence, during live performance, the user can navigate the space of rhythms in between `A` and `B`.

In other words, in this case, the system would work as a sequencer! A sequencer that is ofcourse programmed in a very different way than traditional sequencers!


<img src="/assets/ready-to-use-apps/GrooveTransformer/AB_Interp.png" alt="Thumbnail" width="50%">


### Reacting to a Live Rhythmic Source

While operating in this mode is interesting, we can take this idea further by introducing a third pattern, `G`, which is obtained from an incoming rhythmic pattern in real-time. 
This means that not only can we interpolate between `A` and `B` which are most-likely pre-programmed, but also we can use a rhythmic pattern that dynamically changes during the performance.
Hence, the system can also _**<u>accompany</u>**_  an incoming rhythmic pattern!

<img src="/assets/ready-to-use-apps/GrooveTransformer/ABG_Via_Sliders.png" alt="Thumbnail" width="50%">


    The best way to think about this is that the system can playback pre-programmed patterns, while also adapting the playback to a live rhythmic source in real-time.


The introduction of the third pattern results in a triangular space, where the user can navigate between the three patterns.


<img src="/assets/ready-to-use-apps/GrooveTransformer/overview_1.png" alt="Thumbnail" width="50%">


In this space, each region will have varying degrees of influence from the three patterns, `A`, `B`, and `G`.

<img src="/assets/ready-to-use-apps/GrooveTransformer/ABG_Interp_Annotated.png" alt="Thumbnail" width="50%">


What's interesting is that at the edges of the space, only two of the three corner patterns will be influential, hence allowing the user to not only modify the generations but also dynamically modify the role of the system in the performance.
That is, to decide whether the system should be a sequencer, an accompaniment generator, or a hybrid of the two!




<img src="/assets/ready-to-use-apps/GrooveTransformer/overview_3.png" alt="Thumbnail" width="50%">





### Where does the Live Rhythmic Source come from?

The model was trained on rhythmic patterns that were extracted from drum patterns. This means that the model is first and foremost trained on rhythmic patterns that are "drum-like".

That said, in reality, we can extract this rhythmic pattern from any source, such as a drum loop, a melody, or even a speech! 

While trained on MIDI sequences, we have external processes that allow for automatic extraction of rhythmic patterns from audio sources.

Keep in mind that the rhythm extraction from audio sources is not perfect, and it works best with very transient (percussive) sources.
 
<img src="/assets/ready-to-use-apps/GrooveTransformer/overview_4.png" alt="Thumbnail" width="50%">


### Manual or Automatic Navigation

During the performance, the user can manually navigate the space, and the system immediately reacts to the movement. 

We also have implemented mechanisms that allow for automatic navigation of the space, in case the user desires to focus on other aspects of the performance.

In this case, the system will automatically interpolate between the three patterns, `A`, `B`, and `G`, based on a set of rules that are implemented in the plugin.

<img src="/assets/ready-to-use-apps/GrooveTransformer/overview_5.png" alt="Thumbnail" width="50%">


### Manipulating the Generations

One of the most interesting aspects of the plugin is that the user can manipulate the generations in real-time.

This means that for any given point in the space, the user can modify/re-render the drum loop, using a number of controls that are available in the plugin.

A set of "style" buttons allow manipulation of the overall velocity/timing/density of the drum loop. 

Also, a separate set of controls allow for quick manipulation of voicing of the generations, while **trying** to keep the overall feel of the loop.


<img src="/assets/ready-to-use-apps/GrooveTransformer/overview_2.png" alt="Thumbnail" width="50%">


We'd love to hear your thoughts on the system, and we are always open to suggestions on how to improve the system! Please feel free to [reach out to us]({{site.BaseUrl}}/ready-to-use-apps/groovetransformer-vst/#contact)!