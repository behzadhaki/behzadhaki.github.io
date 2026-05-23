
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

$$ x[n] \xrightarrow{\text{FRFT}(\alpha)} X[k] \xrightarrow{\text{FRFT}(-\alpha)} x[n] $$

### Index Additivity

The index additivity property of the FRFT states that applying two FRFTs in sequence with angles α₁ and α₂ is equivalent to applying a single FRFT with the sum of those angles:

$$ \text{FRFT}(\alpha_2) \circ \text{FRFT}(\alpha_1) = \text{FRFT}(\alpha_1 + \alpha_2) $$

Note that this essentially implies that the order of the transforms does not matter, as long as the total angle is the same:

$$ \text{FRFT}(\alpha_2) \circ \text{FRFT}(\alpha_1) = \text{FRFT}(\alpha_1) \circ \text{FRFT}(\alpha_2) $$


### Complex-Valued Output

Hence, if we start an audio signal (i.e. a real-valued time-domain waveform) and apply the FRFT with a non-integer α, we get a complex-valued output that contains both magnitude and phase information. 
We can then manipulate this output in various ways (e.g. apply filters, perform convolution, multiply with another signal) and then apply the inverse FRFT (i.e. FRFT with -α) to return to the time domain, resulting in a transformed audio signal that incorporates the effects of our manipulations in the fractional domain.

$$ x[n] \xrightarrow{\text{FRFT}(\alpha)} X[k] \xrightarrow{\text{Manipulation}} \tilde{X}[k] \xrightarrow{\text{FRFT}(-\alpha)} \tilde{x}[n] $$

While this is the most straightforward way to use the FRFT for audio processing, we can also directly output the complex-valued result of the FRFT without applying an inverse transform.
In such cases, we can take the real part of the output and use it as an audio signal directly.

$$ x[n] \xrightarrow{\text{FRFT}(\alpha)} X[k] \xrightarrow{\operatorname{Re}} \operatorname{Re}(X[k]) $$

### Windowing and Overlap

FRFT is not a sample-wise operation. Similar to spectral processing techniques like the Short-Time Fourier Transform (STFT), 
to process longer audio signals in real-time, we apply the FRFT to windowed segments of the input signal with a certain amount of overlap between consecutive windows.

The choice of window size, overlap, and windowing function (e.g. Hann, rectangular) can significantly affect the resulting sound, as they determine how the chirp structures evolve and blend across time.


## FRFT External Overview

To be able to use the FRFT in real-time audio processing and synthesis contexts, we have developed a dedicated Max external called `frft`.

The external has been designed to work within Max's pfft~ framework. 

Here is a simple patch that demonstrates how to use the `frft` external within a pfft~ patcher environment:

<img src="/assets/works/RT_FRFT/pfft_basic_patch.png" alt="Description" width="45%">


{: .note }
pfft~ is a powerful tool in Max for performing spectral processing on audio signals. 
pfft~ has built-in support for specialized windowing, overlap, and buffering mechanisms that allow for efficient real-time processing of audio streams in the frequency domain.
Of course, the FRFT is not a standard spectral processing technique, however, certain properties of the FRFT allow us to in fact leverage the pfft~ framework for our purposes. 
Below we discuss this in more detail.

### Why does FRFT work within pfft~?

For the intended applications using FRFT, we typically work with windowed segments of `audio` signals, generally in an overlapped manner.

While the pfft~ environments, facilitates overlap-add processing and windowing, it provides the users with the FFT of windowed segments and also requires the results to be provided in the same format (i.e. windowed segments in the frequency domain).

So why is it possible to use the FRFT within this framework?

The answer lies in one of the main mathematical properties of the FRFT that we've discussed previously (index additivity).

Let's look at the example patch above. In this patch, a given window of audio goes through the following chain of operations:

1. The input audio signal is windowed and transformed to the frequency domain by fftin~ (i.e. FFT).
2. The output of fftin~ is then fed into the `frft` external, which applies the FRFT with a specified α to the input.
3. The output of the `frft` external is then fed into fftout~, which applies the inverse FFT to return to the time domain and outputs the processed audio signal.

$$ x_w[n] \xrightarrow{\text{FFT}} X[k] \xrightarrow{\text{FRFT}(\alpha)} \tilde{X}[k] \xrightarrow{\text{Inverse FFT}} \tilde{x}_w[n] $$

Now remember that FFT and FRFT are equivalent to FRFTs with specific α values (FFT is FRFT with α = 1, and inverse FFT is FRFT with α = -1).

Therefore, the above chain of operations can be rewritten as:

$$ x_w[n] \xrightarrow{\text{FRFT}(1) \circ \text{FRFT}(\alpha) \circ \text{FRFT}(-1)} \tilde{x}_w[n] $$

Which using the index additivity property of the FRFT can be simplified to:

$$ x_w[n] \xrightarrow{\text{FRFT}(1+\alpha-1)=\text{FRFT}(\alpha)} \tilde{x}_w[n] $$

So, while all data within the pfft~ environment is technically provided in the frequency domain, the input fft/ifft (fftin~/fftout~) operations effectively cancel each other out; 
this is as if we had directly applied the FRFT to the windowed audio segment in the time domain!


### Limitations and Considerations

While pfft~ simplifies the windowing/overlap management, it also imposes certain constraints on how we can use the FRFT.

First, the pfft~ framework only works with window sizes that are powers of two, which may limit the range of window sizes we can use for FRFT processing.

Second, while we can dynamically modify the window settings, everytime we do so, the pfft~ environment needs to be re-initialized, which can cause audio dropouts.

Thirdly, the pfft~ framework involves two FFT operations (fftin~ and fftout~) in the processing chain, which for our purposes are essentially redundant due to the index additivity property of the FRFT. 
This means that we are doing more computations than necessary, which can increase the CPU load and reduce the efficiency of our processing.

{: .note }
We are planning to develop a standalone FRFT external that does not rely on the pfft~ framework, which will allow us to bypass these limitations and optimize the processing chain for FRFT-specific applications.
However, in such case, all operations will be handled within the external, meaning that the underlying chain of operations will not be exposed to the user, hence won't be modifiable.
As such, we believe the current pfft~-based implementation strikes a good balance between flexibility and usability for a wide range of applications, while also allowing users to experiment with the FRFT in real-time audio contexts without needing to worry about the underlying complexities of the transform.

## Applications


### α-synthesis

#### Method

α-synthesis applies the FRFT to a **synthesized input signal** (e.g. sine, square, triangle, sawtooth) to generate complex, dynamically evolving sounds from scratch.

Even a single pure tone at a non-integer α produces a rich chirp-like texture — a horizontal line in the time domain becomes a set of diagonal structures in the spectrogram. The spectral richness of the input directly determines the complexity of the output: harmonically richer waveforms (e.g. sawtooth) produce denser, more layered textures.

The range α ∈ (0, 1) covers the most varied and musically useful territory; values outside this range mirror or repeat these textures due to the rotational symmetry of the transform.

#### Implementation



### α-processing

#### Method

α-processing applies the same FRFT chain to an **existing audio recording or live input** rather than a synthesized signal. The FRFT acts as a spectral transformation effect: at α = 0 the signal passes through unchanged; at α = 1 it is fully transformed to the frequency domain (heard as its magnitude spectrum); at non-integer α, the signal acquires chirp-like modulations whose character depends on the spectral content of the source.

Percussive, tonal, and noisy sources each respond differently — tonal sources tend to produce clean chirp structures, while noise-like sources smear into continuously evolving textures.

#### Implementation



### α-RM (Ring Modulation)

#### Method

α-Ring Modulation transforms **two independent signals into different fractional domains** (α₁ and α₂), multiplies them pointwise in those domains, and outputs the **real part of the result directly** — without applying an inverse FRFT:

$$x_1[n] \xrightarrow{\text{FRFT}(\alpha_1)} X_1[k]$$

$$x_2[n] \xrightarrow{\text{FRFT}(\alpha_2)} X_2[k]$$

$$\text{Output} = \operatorname{Re}\bigl(X_1[k] \cdot X_2[k]\bigr)$$

Because the two signals are transformed to *different* fractional angles before multiplication, the result combines the chirp structures of both in a non-linear way, producing sidebands and interaction textures that are distinct from classical time-domain ring modulation.

#### Implementation



### α-Convolution

#### Method

α-Convolution transforms **two signals to the same fractional domain**, multiplies them, and then applies the **inverse FRFT** (i.e. FRFT with −α) to return to the time domain:

$$x_1[n] \xrightarrow{\text{FRFT}(\alpha)} X_1[k], \quad x_2[n] \xrightarrow{\text{FRFT}(\alpha)} X_2[k]$$

$$Y[k] = X_1[k] \cdot X_2[k] \xrightarrow{\text{FRFT}(-\alpha)} y[n]$$

At α = 1 this is identical to standard frequency-domain convolution. At other values of α, the convolution is performed along a rotated axis in the time-frequency plane, which can impose the spectral envelope of one signal onto the chirp structure of the other in ways that standard convolution cannot.

#### Implementation



### α-Filtering

#### Method

α-Filtering takes a signal to a chosen fractional domain, applies a **filter response H[k]** pointwise, and then returns to the time domain via the inverse FRFT:

$$x[n] \xrightarrow{\text{FRFT}(\alpha)} X[k] \xrightarrow{\times\, H[k]} \tilde{X}[k] \xrightarrow{\text{FRFT}(-\alpha)} \tilde{x}[n]$$

At α = 1 this reduces to standard frequency-domain filtering. At other values of α, the filter mask is applied along a rotated axis — enabling filter shapes that would be impossible in the standard frequency domain, such as filtering out specific chirp rates while preserving others.

#### Implementation



### MaxForLive Integration

