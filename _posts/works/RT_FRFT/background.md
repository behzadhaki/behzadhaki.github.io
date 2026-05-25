
## Theoretical Background on FRFT

We have prepared a comprehensive tutorial on the theory and applications of the Fractional Fourier Transform (FRFT) in sound synthesis and processing, 
which we highly recommend going through before diving into the implementation details of this package:

<div class="works-card-grid--horizontal">
  {% assign tutorial = site.posts | where: "title", "Synthesis Using Fractional Fourier Transform (FRFT)" | first %}
  {% if tutorial %}{% include display_post_card.html doc=tutorial layout="horizontal" %}{% endif %}
</div>

In this post, we will briefly summarize the key concepts of the FRFT and then focus on the specific methods and implementation details of our real-time Max external and Max for Live device.

## FRFT Recap

### What is the FRFT?

As discussed in the tutorial linked above, the FRFT can be thought of as a rotation in a conceptual 2D time-frequency plane. 

Where the standard Fourier Transform (FT) corresponds to 90-degree rotations in this plane (e.g. from time to frequency domain), the FRFT allows for arbitrary angles of rotation, controlled by the parameter α.

That means that the FRFT can produce representations that are intermediate between the time and frequency domains.

<div style="margin:1em 0; width:100%; max-width:400px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_rotation.html?w=400&h=400&wave=sweep&disp=scope&dalpha=0.333&win=hann&freq=440"
          style="width:100%; height:400px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

The location of the output in the time-frequency plane depends on the value of α (called the fractional order or rotation factor). 

### Special Cases

For special integer values of α, the FRFT reduces to familiar operations:

| α value | Operation |
|---------|-----------|
| 0 | Identity — signal is unchanged |
| 1 | Standard Fourier Transform |
| 2 | Time reversal |
| 3 | Inverse Fourier Transform |

### Inverse Operation

Unlike the standard FT, which has a dedicated inverse operation, the FRFT is self-invertible: applying the FRFT with a negative α undoes the transformation:

$$ x[n] \xrightarrow{\mathcal{F}^{\alpha}} X[k] \xrightarrow{\mathcal{F}^{-\alpha}} x[n] $$

### Index Additivity

The index additivity property of the FRFT states that applying two FRFTs in sequence with angles α₁ and α₂ is equivalent to applying a single FRFT with the sum of those angles:

$$ \mathcal{F}^{\alpha_2} \circ \mathcal{F}^{\alpha_1} = \mathcal{F}^{\alpha_1 + \alpha_2} $$

Note that this essentially implies that the order of the transforms does not matter, as long as the total angle is the same:

$$ \mathcal{F}^{\alpha_2} \circ \mathcal{F}^{\alpha_1} = \mathcal{F}^{\alpha_1} \circ \mathcal{F}^{\alpha_2} $$


### Complex-Valued Output

Hence, if we start an audio signal (i.e. a real-valued time-domain waveform) and apply the FRFT with a non-integer α, we get a complex-valued output that contains both magnitude and phase information. 
We can then manipulate this output in various ways (e.g. apply filters, perform convolution, multiply with another signal) and then apply the inverse FRFT (i.e. FRFT with -α) to return to the time domain, resulting in a transformed audio signal that incorporates the effects of our manipulations in the fractional domain.

$$ x[n] \xrightarrow{\mathcal{F}^{\alpha}} X[k] \xrightarrow{\text{Manipulation}} \tilde{X}[k] \xrightarrow{\mathcal{F}^{-\alpha}} \tilde{x}[n] $$

While this is the most straightforward way to use the FRFT for audio processing, we can also directly output the complex-valued result of the FRFT without applying an inverse transform.
In such cases, we can take the real part of the output and use it as an audio signal directly.

$$ x[n] \xrightarrow{\mathcal{F}^{\alpha}} X[k] \xrightarrow{\operatorname{Re}} \operatorname{Re}(X[k]) $$

### Windowing and Overlap

FRFT is not a sample-wise operation. Similar to spectral processing techniques like the Short-Time Fourier Transform (STFT), 
to process longer audio signals in real-time, we apply the FRFT to windowed segments of the input signal with a certain amount of overlap between consecutive windows.

The choice of window size, overlap, and windowing function (e.g. Hann, rectangular) can significantly affect the resulting sound, as they determine how the chirp structures evolve and blend across time.
