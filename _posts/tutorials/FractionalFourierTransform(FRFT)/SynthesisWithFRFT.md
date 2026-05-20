
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

So far we just applied a single FRFT to a single source and listened to the real part of the resulting signal. However, there are many other ways to use the FRFT for synthesis and processing.

For exmaple, we can manipulate a signal in alpha domain and then apply the inverse FRFT to listen to the resulting sound directly in time domain.

$$x[n] \xrightarrow{\text{FRFT}(\alpha)}X[k] \xrightarrow{\text{Manipulation}} \tilde{X}[k] \xrightarrow{\text{FRFT}(-\alpha)} \tilde{x}[n]$$

Alternatively, instead of applying FRFT to a single source, we can apply it to multiple sources and combine the resulting spectra in different ways to create new sounds.
The two sounds can be combined either in the same alpha domain or in different alpha domains. 
If the two sources are transformed to the same alpha domain, we can listen to the result in the time domain directly by applying the inverse FRFT to the resulting spectrum.
If they are transformed to different alpha domains, we can listen to the real part of the resulting spectrum directly in alpha domain without applying the inverse FRFT.

Here are some examples of these different methods:

#### Filtering

In filtering, we take a signal to the alpha domain, apply a filter to it, and then bring it back to time domain.

$$x[n] \xrightarrow{\text{FRFT}(\alpha)}X[k]$$

$$H[k] = \text{Filter Response}$$

$$Y[k] = X[k] \cdot H[k]$$

$$Y[k] \xrightarrow{\text{FRFT}(-\alpha)} \text{Filtered Signal}$$

#### Convolution

In convolution, we take two signals to the same alpha domain, multiply them together, and then bring the result back to time domain.

$$x_1[n] \xrightarrow{\text{FRFT}(\alpha)}X_1[k]$$

$$x_2[n] \xrightarrow{\text{FRFT}(\alpha)}X_2[k]$$

$$Y[k] = X_1[k] \cdot X_2[k]$$

$$Y[k] \xrightarrow{\text{FRFT}(-\alpha)} \text{Convolution Result}$$

#### Ring Mod

In ring modulation, we take two signals to different alpha domains, multiply them together, and then listen to the real part of the resulting signal directly in alpha domain.

$$x_1[n] \xrightarrow{\text{FRFT}(\alpha_1)}X_1[k]$$

$$x_2[n] \xrightarrow{\text{FRFT}(\alpha_2)}X_2[k]$$

$$Y[k] = X_1[k] \cdot X_2[k]$$

$$Y[k] \xrightarrow{\text{Real Part}} \text{Ring Mod Output}$$



### Half-Spectrum Synthesis/Processing

The FRFT assumes a full spectrum representation (i.e. both positive and negative frequencies). In all the demos so far, we have been using the full spectrum for synthesis and processing. 

Despite that FRFT internally assumes a full spectrum, we can still feed it with a half spectrum (i.e. only positive frequencies) and it will still work. 
That said, the resulting sounds will be different from the one obtained by feeding it with a full spectrum.

We suggest going back through some of the demos above and modify the full/half spectrum setting to see how it affects the resulting sound.


## Using FRFT in Real-Time

We have developed a real-time version of the FRFT dedicated for MAX/MSP and Max for Live. 

Please refer to the following link to read more about this:



