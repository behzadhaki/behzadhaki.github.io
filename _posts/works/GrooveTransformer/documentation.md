
## Setup in DAW

As of [VST3](https://steinbergmedia.github.io/vst3_dev_portal/pages/Technical+Documentation/About+MIDI/Index.html), 
there is no MIDI-only plugin type, there are all only instrument or audio effect plugins.

GrooveTransformer has been designed as an audio effect plugin, despite the fact that it does not process audio.

This means that you will need to route MIDI/Audio to the plugin. Below is a quick guide on how to set up GrooveTransformer in your DAW.

If you place GT on a MIDI track, you can only route MIDI into it, but if you place it on an audio track, you can route both MIDI and audio into it.

In Ableton Live, the best way to set up GrooveTransformer is as follows:

<img src="/assets/works/GrooveTransformer/AbletonSetup.png" alt="Thumbnail" width="30%">

The above setup allows to route both MIDI and audio into GrooveTransformer.

{: .warning }
The plugin does not pass audio through it, so do not place it on a track where you want to process audio.

## Manual (Version 0.0.1)

Below is a detailed description of the GrooveTransformer module. 

{: .note}
When hovering the mouse on any control parameter of the plugin, a brief description of the control shows up at the bottom of the plugin.

### Feeding a Live Rhythm to GrooveTransformer

As shown in the setup above, the first track receives MIDI and routes it into GrooveTransformer. Moreover, the GrooveTransformer is always "listening" to the audio coming out of the second channel.

The live rhythm can be in any form you desire, that is it can come from pre-programmed MIDI clips, a live performance on a MIDI controller, a pre-recorded audio loop/track, or a live audio input.

{: .note }
1. In case of audio, the plugin tries to detect the transients into rhythmic information. This is not perfect and may not work well with all types of audio. 
This detection is quite **sensitive to the volume** of the audio stream and the **timbre/attack** of the sounds in the audio stream.
2. Audio detection only works if the host's sample rate is **44100 Hz**. If the sample rate is different, the plugin will not detect audio.
3. The plugin registers the events with respect to a 32-step 16th note grid (i.e. 4/4 time signature with 16 steps per bar). 
As a result, initially to understand the behaviour better, maybe it's best to synchronize with the internal clock of the DAW using a click track.

### Manipulating the Detected Rhythmic Events

<img src="/assets/works/GrooveTransformer/InputManager.gif" alt="Thumbnail" width="30%">

The input rhythmic events are extracted and placed in a 32-step 16th note grid, visible in the top section of the plugin.

This input "buffer" works in an overdub fashion, meaning that the incoming events are added to the buffer, and the buffer is not cleared until the user clears it, or after a certain number of bars specified by the user (Slider left of the looper).

Moreover, there is an "Adaptive Memory" button that, if enabled, will automatically decide how long the events should be kept in the buffer. If a lot of notes are coming in within a short time, the buffer will be cleared faster, and if the notes are sparse, the buffer will be cleared slower.

{: .note }
If you want the plugin to only react to the latest 2-bar rhythm, disable "Adaptive Memory" and move the slider to the lowest value.

The velocity of the registered events can be adjusted using the "Groove Velocity" slider. In the middle, the velocity is kept as is, moving to the upper side increases the velocity, and moving to the lower side decreases the velocity.

The micro-timing of the events can be adjusted using the "Groove Timing" slider. In the lowest position, the micro-timing is kept as is, while moving towards the upper side, moves the events closer and closer to the grid. That is, at the highest position, the events are quantized to the 16th note grid (i.e. no micro-timing).

{: .note }
When saving a preset, the input buffer is not saved. This is to ensure that the user can start fresh with a new rhythm when loading a preset.

{: .note }
If a preset is changed during a performance, the input buffer is kept as is (although the controls may change depending on the preset).

{: .note }
The input buffer is cleared when the plugin is turned off. This has been a deliberate design choice to ensure that the top corner is always associated with a live incoming rhythm. 

### Selecting A/B Patterns

There are a number of ways to select the A/B patterns:

_**<u>Randomization</u>**_: Press the "Dice" button to randomize the A or B pattern. When auditing the A/B patterns, ensure that the playback position is at the corner where the A/B patterns are being randomized.

<img src="/assets/works/GrooveTransformer/AB_Randomization.gif" alt="Thumbnail" width="30%">

_**<u>Snapping to A/B Patterns</u>**_: Next to each corner, there is a snap button (shown with a paperclip icon). Pressing this button will snap the current playback rhythm to either of the A/B slots. This is useful when you want to save a rhythmthat you like. Note that as soon as snap is pressed, the rhythm is saved in the respective slot and the playback position is moved to the corner at which the snap was pressed.

<img src="/assets/works/GrooveTransformer/AB_Snap.gif" alt="Thumbnail" width="30%">

_**<u>Programming via a Groove</u>**_: As mentioned before, the top point corresponds to the live incoming rhythm. This means that, placing the playback at the very top, you can a feed a live rhythm into the plugin and listen to the generation. Whenever you like the generated rhythm, you can snap it to the A/B slots.

<img src="/assets/works/GrooveTransformer/GrooveSnap.gif" alt="Thumbnail" width="30%">

### Navigation of the Triangular Rhythm Space

_**<u>Manual Navigation</u>**_: The most straightforward way to navigate the triangular rhythm space is by manually moving the playback position within the triangular area. 
This is done by either clicking anywhere within the triangular area or by dragging the playback position.

<img src="/assets/works/GrooveTransformer/DragginNav.gif" alt="Thumbnail" width="30%">

_**<u>Navigation Via Host</u>**_: The triangular area is controlled using two parameters called <u>Interpolate</u> and <u>Follow</u>. These are exposed to the host, so you can either map these to a controller, automate them, or use modulation sources to control them.

<img src="/assets/works/GrooveTransformer/HostParamNav.gif" alt="Thumbnail" width="30%">

_**<u>Oscillating between A/B</u>**_: You can find a slider below the triangular area called <u>AB Oscillation Rate</u>. When moved anywhere but the very left, the playback position will oscillate between the A and B patterns at the specified rate. This is similar to modulating the <u>Interpolate</u> parameter externally from the host.

<img src="/assets/works/GrooveTransformer/ABOscillation.gif" alt="Thumbnail" width="30%">

_**<u>Adaptive Follow</u>**_: A button called <u>Adaptive Follow</u> is provided to automatically adjust the <u>Follow</u> parameter based on the incoming rhythm. The way it works is that as the groove becomes more active (dense), the playback position moves more and more towards the top of the triangle. 
The highest point reached by the playback position is determined by a slider called <u>Max Follow</u>, placed below the Adaptive Follow button.

<img src="/assets/works/GrooveTransformer/AdaptFollow.gif" alt="Thumbnail" width="30%">

{: .note } 
The combination of Adaptive Follow, Adaptive Memory, and AB Oscillation can lead to full autonomous navigation of the triangular rhythm space.

{: .note }
While Adaptive Follow and AB Oscillation are engaged, the user can still manually navigate the triangular rhythm space. The manual navigation will override the automatic navigation and automatically disengage the Adaptive Follow and AB Oscillation Rate. 

### Manipulation of Generations Using Controls

_**<u>Style Templates</u>**_: The plugin comes with 9 style controls that can be used to manipulate the generated rhythm. We intentionally did not name these controls to promote experimentation, rather than imposing the notion of what style the performance should stick to! 
The style templates manipulate the generated patterns in terms of velocity, timing, voice density, and voice distribution. Hence, they can quite drastically change the feel of the generated rhythm.

<img src="/assets/works/GrooveTransformer/StyleControls.gif" alt="Thumbnail" width="30%">

_**<u>Voicing</u>**_: The voicing controls are used to manipulate the voice distribution of the generated rhythm. 
The 9-drum voices are grouped into 5 categories:

| Category | Drum Voices |
|----------|-------------|
| Kick     | Kick Drum   |
| Snare    | Snare Drum  |
| Hat      | Closed Hat, Open Hat|
| Tom      | Low Tom, Mid Tom, High Tom |
| Cymbal   | Crash, Ride |
|-|-|

For each category, the groups can be <u>Muted</u> or <u>Redistributed</u>. 

Muting simply removed the drum voices from the generated rhythms while keeping the rest as is.

<img src="/assets/works/GrooveTransformer/VoiceMute.gif" alt="Thumbnail" width="30%">

Redistribution, on the other hand, takes out the drum voices from the category and tries to render a new pattern that ideally "feels" the same however without the removed drum voices.

<img src="/assets/works/GrooveTransformer/VoiceRedistribute.gif" alt="Thumbnail" width="30%">

{: .note }
Redistribution is done using the generative model. As such, at times it may not work as expected! 

{: .note }
Also, whether the redistributed pattern feels the same is also quite dependent on the synthesis

{: .note} 
A Note on Style and Voicing Controls: These controls are applied globally, that is, all the patterns within the rhythmic space are modified using these controls. 
This was a deliberate design choice to ensure that the controls impact the immediate pattern, hence, being highly geared towards real-time performance. 

_**<u>Generation Quantization</u>**_: The micro-timings of the generations can be quantized using the <u>Generation Quantization</u> slider placed in the bottom right corner of the plugin. 
At the very left, there is no quantization while at the very right all events are snapped to the 16th note grid (hence, no micro-timing). 

<img src="/assets/works/GrooveTransformer/GenQuantization.gif" alt="Thumbnail" width="30%">

### Trying Model Variants

There are three model variants that can be used. These models have the same architecture, with different training schemes. 
It's not necessary to go through the technical differences, but what is perhaps important is that the models were trained with the following aims:

| Category | Drum Voices                                                               |
|----------|---------------------------------------------------------------------------|
| 0.2Beta  | Trained for better conversion of live incoming rhythm into a drum pattern |
| 1.0Beta  | Trained for better generation of random drum pattern patterns             |
| 0.5Beta | Trained to be somewhere in between the above two |

{: .warning}
Once a model is swapped mid-session, the patterns at A/B positions will be changed and will have no correlation with the previous patterns. 

It's not to say that you shouldn't swap the model mid-session, just be aware of the behaviour!

If you are using the model only for accompaniment generation (i.e. playback is always at the very top), the generations will likely change, but will still be correlated with the groove buffer. Hence, in this case, it is "safe" to change the model. 