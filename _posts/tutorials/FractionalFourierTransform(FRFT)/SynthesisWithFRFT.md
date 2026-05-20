
## Basic Synthesis and Processing with FRFT
 
In fact, in many of the examples we have seen so far, we have been using the FRFT for synthesis and processing without explicitly mentioning it.

In these examples, we discussed how we can create (i.e. synthesize) quite complex dynamically evolving sounds by simply applying FRFT to simple signals such as a pure tone.  

While for simplicity, we usually focused on pure tone inputs, we occasionally discussed that we can use more harmonically rich signals.

The following demo allows you to experiment with different input waveforms and listen to the resulting sound after applying FRFT to them.

<div style="width:100%; max-width:800px;">
  <iframe src="/assets/web/frft/demos/embed_interactive_frft.html?w=800&h=220&dur=10&alpha=0.05&type=triangle&blocksize=65536&overlap=4"
          style="width:100%; height:220px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

Moreover, we can use the same processing chain for sound processing as well. That is, instead of synthesizing complex sounds
from simple inputs, we can take an existing sound and apply FRFT to it to get a transformed version of the original sound. 

Here are some example of processing audio recordings with FRFT:

<div style="width:100%; max-width:800px;">
  <iframe src="/assets/web/frft/demos/embed_interactive_frft.html?w=800&h=220&dur=10&alpha=0.05&type=file&blocksize=65536&overlap=4&url=/assets/web/frft/audio/613395__elzozo__double-bass-glissendo-upright-bass.m4a"
          style="width:100%; height:220px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

<div style="width:100%; max-width:800px;">
  <iframe src="/assets/web/frft/demos/embed_interactive_frft.html?w=800&h=220&dur=10&alpha=0.01&type=file&blocksize=16384&overlap=4&url=/assets/web/frft/audio/628817__owstu__female-vocal-long.wav"
          style="width:100%; height:220px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

{:.note} 
The audio demos here correspond to the following freesound.org recordings: [https://freesound.org/people/elzozo/sounds/613395/](https://freesound.org/people/elzozo/sounds/613395/) and [https://freesound.org/people/owstu/sounds/628817/](https://freesound.org/people/owstu/sounds/628817/)

## A Few Final Notes

### Other Ways to Use FRFT for Synthesis/Processing



### Half-Spectrum Synthesis/Processing

## Using FRFT in Real-Time

We have developed a real-time version of the FRFT dedicated for MAX/MSP and Max for Live. 

You can read more about it here:

