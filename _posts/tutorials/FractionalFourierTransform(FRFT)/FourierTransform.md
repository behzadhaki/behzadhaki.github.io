
Let's start with a quick refresher on the Fourier Transform (FT). 

## What is Fourier Transform?
The FT is a mathematical transformation that decomposes a signal into its constituent frequencies. 

Basicaly, `FT` transforms a `time-domain` signal into a `frequency-domain` representation. 

For instance, if you have a pure tone at 1000 Hz, FT results in a representation such as the following:

<div style="margin:1em 0; width:100%; max-width:600px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_fft_spectrum.html?w=600&h=220&type=sine&win=exact&freq=1000"
          style="width:100%; height:220px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

In this repesentation, the x-axis corresponds to frequency, and the y-axis corresponds to the amplitude of each frequency component.
Now, if you add harmonics to the pure tone, you will get a more complex spectrum (try it out by changing the waveform type in the demo above).


{:.note}
FT results in a complex-valued signal, here we are only showing the magnitude of this complex signal for simplicity.


{:.note}
When we perform FT on a real signal (like an audio signal), we get a spectrum that is symmetric (as in the example above). 
In such cases, commonly we work with the positive frequencies (the right half of the spectrum) since the negative frequencies are just a mirror image of the positive ones.
That said, in this tutorial, we will be working with the full spectrum. This will be important when we discuss Fractional Fourier Transform (FRFT) later on. 

## Fourier Transform for Synthesis and Processing

There are many applications of the FT in sound synthesis and processing. 

Most common methods rely on the inversibility of the FT, which means that we can transform a signal to the frequency domain and also perform the inverse operation to get back to time domain.

$$x[n] \xrightarrow{\text{FT}} X[k]  \xrightarrow{\text{IFT}} x[n]$$

With this property, we can synthesize/process sounds by applying IFT to a spectrum created from scratch or a spectrum obtained from an existing signal, 

$$ Y[k] \xrightarrow{\text{IFT}} y[n]$$

$$x[n] \xrightarrow{\text{FT}} X[k]  \xrightarrow{\text{Manipulation}} \tilde{X}[k] \xrightarrow{\text{IFT}} \tilde{x}[n]$$

{:.note}
The frequency-domain signals are generally complex-valued, which means that they have both a real part and an imaginary part.
To ensure that the resulting time-domain signal is real-valued, the complex spectrum must satisfy the conjugate symmetry property, which states that the negative frequency components are the complex conjugate of the positive frequency components:
$$X[-k] = X[k]^*$$

## Treating Fourier Transform Components as Audio Signals

In the above examples, to listen to the spectrum, we applied the IFT to the complex spectrum to get back to the time domain.

However, it is also possible to listen to the real, imaginary parts of the complex spectrum directly without applying IFT.  

$$ x[n] \xrightarrow{\text{FT}} X[k] \xrightarrow{\text{Real Part}} \text{Re}\{X[k]\} $$

or 

$$ x[n] \xrightarrow{\text{FT}} X[k] \xrightarrow{\text{Imaginary Part}} \text{Im}\{X[k]\} $$

**In other words, we treat the real or the imaginary component of the complex spectrum as an audio signal directly.**

In the following demo, you can try out different waveforms and listen to the real (or imaginary) part of their Fourier Transform directly, while treating them as audio signals:

<div style="margin:1em 0; width:100%; max-width:600px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_ft_listen.html?w=600&h=220&type=sine&part=imag&freq=440"
          style="width:100%; height:220px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>


Try out different waveforms: sine, square, triangle, and sawtooth. In these cases, the resulting sound is a squence of clicks, 
as the Fourier Transform of these waveforms consists of a series of impulses at the harmonic frequencies.

{:.note}
When interacting with the demo, notice the X-axis transforming from frequency to time as soon as you play the sound.
In the rest of this tutorial, we will be listening to the real part of any complex signal, whether obtained from the FT or any other operation.

## Rotational Behavior of Fourier Transform

As discussed above, the FT transforms a signal from the time domain to the frequency domain. 
Likewise, there is an inverse operation called the Inverse Fourier Transform (IFT) that transforms a signal from the frequency domain back to the time domain.

$$x[n] \xrightarrow{\text{FT}} X[k]  \xrightarrow{\text{IFT}} x[n]$$

An interesting property of the FT is that if we apply the FT four times consecutively, you will get back to the original signal:

$$x[n] \xrightarrow{\text{FT}} X[k] \xrightarrow{\text{FT}} x[-n] \xrightarrow{\text{FT}} X[-k] \xrightarrow{\text{FT}} x[n]$$

To conceptualize this, we can think of the time-frequency plane as a 2D space where the x-axis represents time and the y-axis represents frequency.
As such, applying the FT corresponds to a 90-degree rotation in this plane. The following demo visualizes this rotational behavior of the FT:

<div style="margin:1em 0; width:100%; max-width:400px; background:#1a1a1a; border-radius:8px; overflow:hidden;">
  <iframe src="/assets/web/frft/demos/embed_frft_rotation.html?w=400&h=400&wave=sine&disp=wave&dalpha=dft&win=hann&freq=1004"
          style="width:100%; height:400px; border:none; display:block"
          allow="autoplay">
  </iframe>
</div>

{:.note} 
Press on the waveforms to listen to the corresponding time-domain or frequency-domain signals

{:.note} 
The waveforms at the frequency domain are the real part of the Fourier Transform. 

{:.note} 
To understand the impact of time reversal, use the "Freq sweep" input and also switch to "Spectrogram" visualization.

