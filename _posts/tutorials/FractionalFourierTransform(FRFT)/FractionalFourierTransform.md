
## FRFT as a Generalization of Fourier Transform

We ended the previous section by mentioning that the Fourier Transform (FT) can be thought of as a rotation in a conceptual time-frequency plane.

That is, in this 2D conceptual space, a 90-degree rotation corresponds to a single application of the FT, and
given its rotational behavior, applying the FT four times will bring you back to the original signal.

Now, the question is: **Can we apply a rotation that is not necessarily 90 degrees? If so, what sort of intermediary 
sounds would be achieved?**

This is exactly what the Fractional Fourier Transform (FRFT) allows us to do. 
The FRFT is a generalization of the FT that enables us to perform rotations by arbitrary angles in the time-frequency plane.

Here is an extended version of the previous demo that also allows for intermediate rotations using the FRFT:

<div style="margin:1em 0; width:100%; max-width:400px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_rotation.html?w=400&h=400&wave=sine&disp=scope&dalpha=0.333&win=hann&freq=440"
          style="width:100%; height:400px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

{:.note} 
Notice that in this demo (as opposed to the previous one), instead of showing angles of 0, 90, 180, and 270 degrees, 
we are using integer values of 0, 1, 2, and 3 to represent the same angles. 
This is because in the context of the FRFT, a rotation of 90 degrees corresponds to a value of 1.
We call this value the `fractional order` or `rotation factor` of the FRFT, and we typically denote it by the symbol $\alpha$ (alpha).
$$ \text{Rotation Angle} = \alpha \times 90^\circ $$



{:.note}
Switch between the `Waveform/Spectrogram` tabs to visualize the waveforms or their spectral content at different rotation factors.


Looking at the spectrograms for a single static sine input, you can see that at non-integer values of $\alpha$ (i.e. in between the time and frequency domains), 
the resulting waveforms have a more complex structure. For instance:

    A single tone (visible as a horizontal line in the time domain) is transformed into chirp-like structures (visible as multiple diagonal line in the spectrogram) at intermediate rotation factors.


## Some Useful Properties of FRFT

In this section, we will go over some useful properties of the FRFT that are relevant to sound synthesis and processing.

We won't get into the mathematical details of these properties, but we will provide some intuition and examples to illustrate them. (The paper on which this tutorial is based provides a rigorous mathematical treatment of these properties, so we encourage you to check it out for more details if you're interested.)


### Special Cases of FRFT

We have already discussed that the FRFT is a generalization of the FT, and as such, it has some special cases that correspond to specific values of the rotation factor $\alpha$:

- When $\alpha = 0$, the FRFT reduces to the identity operation, meaning that the output is the same as the input signal.
- When $\alpha = 1$, the FRFT reduces to the standard Fourier Transform
- When $\alpha = 2$, the FRFT corresponds to a reversal operation
- When $\alpha = 3$, the FRFT corresponds to an inverse Fourier Transform

The following demo illustrates these special cases applying the FRFT to a sine sweep input:

<div style="margin:1em 0; width:100%; max-width:400px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_rotation.html?w=400&h=430&wave=sweep&disp=scope&dalpha=1&win=hann&interactive=0"
          style="width:100%; height:430px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

### Inverting the FRFT

Remember that in the case of the FT, we had a dedicated inverse operation called the Inverse Fourier Transform (IFT) that allowed us to transform a signal from the frequency domain back to the time domain.

In the case of the FRFT, there is no separate inverse operation. Instead, the inverse of the FRFT is also a FRFT, but with a negative rotation factor.

$$ x[n] \xrightarrow{\text{FRFT}(\alpha)} X_\alpha[k] \xrightarrow{\text{FRFT}(-\alpha)} x[n] $$

{:.note}
A positive rotation factor $\alpha$ corresponds to a counter-clockwise rotation in the time-frequency plane, 
while a negative rotation factor corresponds to a clockwise rotation.

In the following demo, you can transform a signal into the alpha domain and then apply the inverse transformation to get back to the original signal:

<div style="margin:1em 0; width:100%; max-width:500px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_additivity.html?w=500&h=400&wave=triangle&disp=wave&win=hann&alpha1=0.5&alpha2=-0.5&freq=440&inversion=1"
          style="width:100%; height:400px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

Here you can see that the final output after $\alpha$ and $-\alpha$ transformations is almost identical to the original input signal.

{:.note} 
In this demo, we visualize the error between the two paths. For a perfect mathematically accurate implementation of the FRFT, this error should be zero. 
However, in here, we are using a light-weight implementation of the FRFT which is highly optimized for real-time performance at the cost of some accuracy.
Hence, the error is not exactly zero, but it is still very small and inaudible in most cases. 
That said, in pure mathematical terms, the error should be zero, and the original signal should be perfectly 
reconstructed after applying the FRFT and its inverse.


### Index Additivity

The FRFT has an interesting property called `index additivity`, which states that if you apply two FRFTs with rotation factors $\alpha_1$ and $\alpha_2$ consecutively, it is equivalent to applying a single FRFT with a rotation factor that is the sum of the two individual rotation factors:

$$\begin{array}{c}
x[n] \xrightarrow{\text{FRFT}(\alpha_1)} X_{\alpha_1}[k] \xrightarrow{\text{FRFT}(\alpha_2)} X_{\alpha_1+\alpha_2}[k] \\[6pt]
x[n] \xrightarrow[\text{FRFT}(\alpha_1+\alpha_2)]{\hspace{14em}} X_{\alpha_1+\alpha_2}[k]
\end{array}$$

In the following demo, you can apply two consecutive FRFTs and observe the resulting waveforms and spectrograms at each step, as well as the final result of applying a single FRFT with the combined rotation factor:

<div style="margin:1em 0; width:100%; max-width:500px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_additivity.html?w=500&h=400&wave=sawtooth&disp=scope&win=hann&alpha1=0.15&alpha2=0.62&freq=440"
          style="width:100%; height:400px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

## Impact of Input Signals and $alpha$ on the Resulting Textures

The resulting sounds obtained from applying the FRFT to an input signal can vary greatly depending on the characteristics of the input signal and the chosen rotation factor $\alpha$.

In this part, we will see how the spectral content of a sound, as well as the choice of $\alpha$, can impact the resulting textures obtained from applying the FRFT.

To start with, let's look at the following demo in which we use a sine sweep input signal and apply the FRFT with different values of $\alpha$ to observe the resulting waveforms and spectrograms:

<div style="margin:1em 0; width:100%; max-width:500px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_rotation.html?w=500&h=500&wave=sweep&disp=scope&dalpha=0.333&win=hann"
          style="width:100%; height:500px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

The first observation here is that the spectral content of the textures in the right and left half of the time-frequency plane are mirrored versions of each other. Moreover, similar textures can be obtained in the top-right and bottom-right quadrants.
With these observations in mind, for the remainder of this section, we will focus on the top-right quadrant of the time-frequency plane, which corresponds to fractional orders between 0 and 1 $(\alpha \in [0, 1])$.

In the following demo, for a specific input type, we render many different combinations of $\alpha$ and the input frequency content.
We suggest interacting with the demo and exploring the impact of these parameters on the resulting textures.

<div style="margin:1em 0; width:100%; max-width:600px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_alpha_sweep_frft.html?w=600&h=300&wave=sine&win=hann&halfspec=0&freqidx=3&alpha=0.5"
          style="width:100%; height:300px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

{:.note}
Select the 'BOTH' option, to visualize and listen to the source and transformation concurrently. 
For now, we suggest not modifying the source panel (except for the source type)

We suggest the following steps to explore the impact of $\alpha$ and the input spectral content on the resulting textures:

- At a fixed value of $\alpha$, move the frequency slider to explore the impact of the input spectral content on the resulting textures.
- At a fixed input frequency, move the $\alpha$ slider to explore the impact of $\alpha$ on the resulting textures.
- Try out different waveforms (sine, square, triangle, and sawtooth) to explore the impact of the input waveform on the resulting textures.


## Impact of Windowing

The way we've been applying the FRFT so far is by taking the entire input signal, applying the FRFT to it, and then listening to the resulting output.

That said, just like most spectral processing techniques, the FRFT can also be applied in a windowed manner, where we take a short segment of the input signal (called a window), apply the FRFT to that segment, and then move the window across the entire signal to process it in chunks.

To construct the final output, we can either concatenate the processed segments together (non-overlapping windows) or we can overlap and add the processed segments together (overlapping windows).


### Window Size Vs. Chirp Speed
Let's start with considering this example: Generating a long Sinusoidal signal with a fixed frequency.  
The way we can apply FRFT, is either we apply it to the entire signal at once, or we can chop the signal into smaller non-overlapping segments and apply the FRFT to each segment separately.
Because the spectral content in each of the cases (regardless of the segment size) is the same, visually, the resulting spectrograms look similar. 
However, when we play each of the resulting outputs, the speed at which the textures evolve over time is different.
This can be observed in the following demo in which on the left we use a window size of 131072 samples and on the right we use half this size i.e. 32768 samples):


<div style="margin:1em 0; display:flex; gap:1rem; flex-wrap:wrap;">
  <div style="flex:1; min-width:280px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
    <iframe src="/assets/web/frft/demos/embed_ola_frft.html?w=600&h=250&wave=sine&freq=440&alpha=0.50&blocksize=131072&overlap=1&halfspec=0&lock=1"
            style="width:100%; height:250px; border:none; display:block"
            allow="autoplay">
    </iframe>
  </div>
  <div style="flex:1; min-width:280px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
    <iframe src="/assets/web/frft/demos/embed_ola_frft.html?w=600&h=250&wave=sine&freq=440&alpha=0.50&blocksize=32768&overlap=1&halfspec=0&lock=1"
            style="width:100%; height:250px; border:none; display:block"
            allow="autoplay">
    </iframe>
  </div>
</div>

As you notice, while the spectral content look the same, the textures for the smaller window size (on the right) evolve faster over time compared to the larger window size (on the left).

{:.note} 
The smearing of the spectrum on the write panel is due to the smaller window size, which results in a lower frequency resolution.

### Overlapping Windows

We can also apply the FRFT in an overlapping manner, where we take overlapping segments of the input signal, apply the FRFT to each segment separately, and then overlap and add the processed segments together.
In this case, you can clearly see that the chirp-like structures from one window bleed into the next window:  

<div style="margin:1em 0; width:100%; max-width:600px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_ola_frft.html?w=600&h=250&wave=sine&freq=440&alpha=0.50&blocksize=32768&overlap=4&halfspec=0"
          style="width:100%; height:250px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

Change the `overlap` parameter to see the impact of different overlap amounts on the resulting textures. 
Increasing it, results in faster textures with more chirp-like structures. 

### Effect of Windowing Functions
In these demos, we apply a Hann window to each segment before applying the FRFT, which helps to reduce spectral leakage and create smoother transitions between the segments when they are overlapped and added together.
If you don't apply any windowing function (i.e. use a rectangular window), you will get more abrupt transitions between the segments, which can result in additional chirp-like structures in the spectrograms.

<div style="margin:1em 0; width:100%; max-width:600px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_ola_frft.html?w=600&h=250&wave=sine&freq=440&alpha=0.50&blocksize=32768&overlap=1&halfspec=0&win=rect"
          style="width:100%; height:250px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

[//]: # (### Harmonic Complexity )

[//]: # (In the above examples we've been using a single tone as the input signal, which results in a single chirp-like structure in the spectrograms.)

[//]: # (If we add more harmonics to the input signal, we will get more chirp-like structures in the spectrograms, and the resulting textures will be more complex.)

[//]: # ()
[//]: # (<div style="margin:1em 0; width:100%; max-width:600px;">)

[//]: # (  <iframe src="/assets/web/frft/demos/embed_ola_frft.html?w=600&h=250&wave=triangle&freq=440&alpha=0.50&blocksize=32768&overlap=4&halfspec=0")

[//]: # (          style="width:100%; height:250px; border:none; display:block")

[//]: # (          allow="autoplay">)

[//]: # (  </iframe>)

[//]: # (</div>)





