
GrooveTransformer can be used either as an _**<u>instrument</u>**_ on which you perform (i.e. a _**<u>sequencer</u>**_), a _**<u>(pseudo-)autonomous rhythm generator</u>**_, or anything in between.

Below are some examples of how you can use the GrooveTransformer VST in different scenarios.

{: .note}
The following are just a few examples of how the GrooveTransformer can be used.
We are interested in hearing about your use cases and how you use the GrooveTransformer!

---

# GrooveTransformer as a Sequencer 

## Basic Operation Using A/B Patterns

{: .hint}Refer to [Documentation]({{site.baseurl}}/GrooveTransformer/Documentation/#selecting-ab-patterns) to see how A/B patterns can be programmed.

The simplest way to use the GrooveTransformer is to use the A/B patterns to switch/morph between two different grooves, while also manipulating the generation parameters in real-time. 

In the following example, we simply morph from pattern A to pattern B. 

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/AB_Interpolation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Groove Input Along with A/B Patterns

As mentioned before, GrooveTransformer can also receive rhythmic inputs in real-time, both from Audio and MIDI sources. This allows the sequencer to not only be controlled by you, but also allows it to react to an external rhythmic source.

The external sources can be anything from loops, other sequencers, or a live performance on an acoustic/digital instrument. Again, all of these can be in audio or MIDI format.

In the following example, we have a bass sequence (MIDI) and a drum loop (audio) that we constantly feed to the plugin. During the performance, we control the plugin by navigating the triangular area.

[//]: # (<iframe width="800" width="800" height="600" src="/assets/works/GrooveTransformer/ABG.mp4" frameborder="20" allowfullscreen autoplay="false"></iframe>)

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/ABG.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

Let's make this a bit more interesting. In the following example, we have a few drum loops fed to the GrooveTransformer. We also have two patterns stored in the A/B slots. 
This time, during the performance, we not only navigate the triangular area but also change the patterns in real-time using the voicing controls. 

[//]: # (<iframe width="800" width="800" height="600" src="/assets/works/GrooveTransformer/AccompanimentToPre-arrangedClips.mp4" frameborder="20" allowfullscreen autoplay="false"></iframe>)

[//]: # (<video width="50%" controls>)

[//]: # (  <source src="/assets/works/GrooveTransformer/AccompanimentToPre-arrangedClips.mp4" type="video/mp4">)

[//]: # (  Your browser does not support the video tag.)

[//]: # (</video>)

[//]: # (<iframe width="800" height="600" src="https://www.youtube.com/embed/PqI_d1JYQpU?si=oGSNfsZEo0WnauYl&vq=hd2160&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>)



<img src="/assets/works/GrooveTransformer/GT_SequencerAccompaniment.png" alt="Thumbnail" width="50%">


<div style="max-width: 600px;">
  <iframe 
    src="https://www.youtube.com/embed/PqI_d1JYQpU?si=E7zcWoeCKjKdC7Pb&amp;clip=Ugkxtlok0Ma02HSiY2Gmt2UmrNEA0BRjGzIr&amp;clipt=ELSGFhiU2xk" 
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
    style="width: 100%; height: 338px; border-radius: 8px;">
  </iframe>
</div>



Ok! Let's take it up a notch. So far, we've been using the generations to trigger drum samples. While designed to generate drum patterns, we can use the generations to trigger any kind of sample!

In the following example, we feed a few drum loops to the GrooveTransformer, and we use the generations to trigger two separate sample kits, one containing hand percussion samples and the other containing audio samples that are not necessarily percussive.
During the session, we navigate the triangular area and change the patterns in real-time using the voicing controls.

[//]: # (<iframe width="800" width="800" height="600" src="/assets/works/GrooveTransformer/Non-drum Extra Sequencing.mp4" frameborder="20" allowfullscreen autoplay="false"></iframe>)

[TBD INSERT SESSION OVERVIEW]


<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/Non-drum%20Extra%20Sequencing_trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


What's worth noting is that so far, we've only used mainly percussive sources as inputs. In the case of audio, the GrooveTransformer can also be used to generate accompaniments for melodic instruments as well, that said, depending on the texture and the complexity of the audio, the results may vary.
Specifically, for sounds with slow attack times, the GrooveTransformer may not be able to capture the rhythmic content accurately (or at all). In the following example, we feed non-percussive audio to the plugin and perform on the sequencer same as before. Note that only some of the audio events can be 
detected by the GrooveTransformer, and the rest are ignored.

[TBD INSERT SESSION OVERVIEW]


<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/NonPercussiveAudioInputs_trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>




So far, on the input, we've been using audio/midi sources that were part of the performance (i.e. synthesized). One trick we can do is to feed a looping MIDI groove to the plugin, without synthesizing any sound from it. 
This way, the top corner will also be associated with an "artificially static" groove, and hence, we can perform the sequencer using three "static" patterns, rather than two. 

In the following example, we start from A, morph to B, and then to morph to G (fed with a looping MIDI sequence that is not synthesized). Note that, the pad sounds you hear in this example are not fed to the plugin and are just being played for the sake of the performance.


[TBD INSERT SESSION OVERVIEW]

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/PatternMorph3Grooves_trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

---

# GrooveTransformer as a Pseudo-Autonomous Rhythm Generator

As mentioned in the documentation, there are a number of ways to enable the GrooveTransformer to self-navigate the triangular area.

If this feature is enabled, then the GrooveTransformer can be used as a pseudo-autonomous rhythm generator. 

{: .warning}
We call this **pseudo**-autonomy because we are using some basic rules to navigate this space, hence there is no actual decision-making involved!

In the following example, we don't interact with the plugin directly, except for controlling what is being fed to the input. Specifically, we have some looping patterns prepared; during the performance, we mix between them and feed them to the plugin. 
The plugin then generates the accompaniment based on the input and we synthesize the output accordingly.


[TBD INSERT SESSION OVERVIEW]


<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/AutonomousPerformingClips.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


Alternatively, we can allow the plugin to play a pattern and we can start jamming on top of it, using any instrument we like. Below is an example of how we can use the GrooveTransformer as a pseudo-autonomous rhythm generator, while we play a pattern on an external synthesizer.


<img src="/assets/works/GrooveTransformer/Keyboard%20Accompaniment.png" alt="Thumbnail" width="50%">

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/FullAutoAccomp.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/snippet3_ms20.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

The performance on the external instrument is not limited to performing the keys! In the following example, we are sequencing the external synth and play with the synthesis parameters in real-time.


<img src="/assets/works/GrooveTransformer/SynthAccompaniment.png" alt="Thumbnail" width="50%">


<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/snippet1_ms20_trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


---

# Advanced Use Cases: Going beyond Generating Percussive Sequences


## Parameter Sequencing using Velocity of Generations

Instead of using it as a trigger sequencer, we can use it to sequence parameters of a synthesizer using the velocity of the generations!
In the following example, we have prepared a virtual modular patch (in [VCV Rack](https://vcvrack.com/)) that uses the velocity of the generations to modulate some parameters of the [Mutable Instruments Plaits module](https://mutable-instruments.net/modules/plaits/).


[TBD INSERT SESSION OVERVIEW]


<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/UsingVelocityFeaturesForParameterSequencing.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>



<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/SequencingDrumsAndParams.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>



## Rhythmic Manipulation of Audio

So far, we used the plugin to trigger sounds or modulate parameters of a synthesizer. However, we can also use the GrooveTransformer to manipulate audio in real-time.

For this, we need to make custom processing chains that can take the output of the GrooveTransformer and manipulate it in real-time.

In the following example, we have a custom patch in [VCV Rack](https://vcvrack.com/) that takes the output of the GrooveTransformer and uses the trigger/velocity of the generations to activate three voltage-controlled amplifiers (VCAs). Each VCA is connected to a different audio source, and the output of the VCAs is mixed together.


<img src="/assets/works/GrooveTransformer/GT_ModulationSource.png" alt="Thumbnail" width="50%">

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/RhythmicManipulation%20of%20Audio_trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Multiple Instances of GrooveTransformer
Moreover, we can use multiple instances of the plugin each for a separate purpose. For example, we can use one instance of the GrooveTransformer to generate a drum pattern, and another instance to manipulate audio in real-time.


<img src="/assets/works/GrooveTransformer/GT_ModulationSource.png" alt="Thumbnail" width="50%">

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/ModSource.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## Pitch Sequencing

While the plugin is designed to generate percussive sequences, we can also use it to generate melodic sequences. 
For this, we need to use the plugin in conjunction with a synthesizer that can generate pitched sounds. 
Also, we need to potentially use external MIDI processing to map the output of the GrooveTransformer to the pitch of the synthesizer.

In the following example, we use three instances of the GrooveTransformer to generate three different pitched sequences.
The pitch of the generated sequences are all modulated randomly or via a MIDI controller, and the modulated pitch is then passed through a quantizer. 



<img src="/assets/works/GrooveTransformer/PitchSequencing.png" alt="Thumbnail" width="50%">

<video width="50%" controls>
  <source src="/assets/works/GrooveTransformer/PitchSequencing_trimmed.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>