

## Demo

<video width="50%" controls>
  <source src="/assets/works/MultistreamRhythmicMods/Demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


This patch generates multiple parallel modulation curves that are rhythmically interlocked. 

The idea behind this patch started from the [GrooveTransformer]({{site.baseurl}}/ready-to-use-apps/groove-transformer-vst/). GrooveTransformer generates drum patterns in MIDI format. These patterns can be used to `trigger` MIDI instruments.

In this patch, however, the generated MIDI events are used to create continuous modulation curves by simply fitting a curve to the MIDI events. 

The generated curves can then be used to modulate any parameter in Ableton Live, hence allowing for rhythmic modulations of any parameter in real-time.

## How does it work?

The patch receives generated drum events from the GrooveTransformer vst (via a built-in OSC connection). 

Then the events are subdivided into 5 streams:

- **Stream 1**: Kick pattern
- **Stream 2**: Snare pattern
- **Stream 3**: Hi-hat pattern
- **Stream 4**: Toms pattern
- **Stream 5**: Cymbals pattern

A curve is then fitted to each stream of events. The shape of the curve is controllable to allow for very transiet shapes, all the way to very smooth curves. 

For each stream, 3 destinations can be set. However, if you need more, you can duplicate the max patch and set different destinations for each copy.


## Current Status

The current max patch (shown below) is in early development. It is functional, but it is not yet fully polished. We are currently working on improving the user interface and adding more features.

![](/assets/works/MultistreamRhythmicMods/prototype.png)
