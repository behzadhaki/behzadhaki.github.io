---
layout: page
permalink: /summary/
title: Real-time Drum Accompaniment Generation
description: Summary of my PhD activities so far
nav: false
nav_order: 4
---


<br><br><br>
---
## **Background**
---

The main objective of my PhD has been the **development** of a system that can generate **real-time drum accompaniments for live instrumental performances**.

The idea here was that instead of focusing mainly on the generative process from an architectural perspective, 
I wanted to also focus on the interaction between the system and the performer. 

<img src="{{ site.baseurl }}/assets/img/dev_stages.png" alt="dev_stages" style="width: 700px;"/>


- small models 
- deployed in an easy-to-use environment
- allowing control over the generation process

In order to be able to use small models, we focus on loop generation, 
which is a more constrained task than long-term accompaniment generation.

Also, instead of analyzing the harmonic content of the input, we focus on the rhythmic content.
This will allow us to (1) generate drum accompaniments that are rhythmically interlocked with the input,
and (2) given that we didn't want to create a human-like system, this constraint will naturally limit
the human-like behavior of the system.


<br><br><br>
---
## **1 - Drum Generation Using Transformers**
---

In my first year, we developed an offline long-term drum generation system using Transformer-XL architecture.

<div class="publications">
  {% bibliography -f papers -q @*[key=NIME21_33]* %}
</div>

While the system was able to generate 'realistic' long-term drum patterns, it was not suitable for real-time generation due to the computational complexity of the model. 
Moreover, I wanted to focus on generating drums conditioned on live instrumental performances. 

As such, we decided to re-think our approach and focus on loop generation using smaller models. Inspired with Google Magenta's GrooVAE, 
we explored whether we can use transformers to generate drum loops. Moreover, in order to speed-up the performance in real-time deployment, 
we also explored whether we can avoid tokenization of the input and output sequences. That is, 
whether we could use a very simple representation of our sequences. 

<br> 

> **How to represent drum loops?**
> 
> Grid relative piano-roll representation. Tempo-agnostic, and focus on 4/4 time signature.
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/hvo.jpeg" alt="hvo" style="width: 700px;"/>

<br> 

> **How to condition on live performances?**
> 
> Use a simple rhythm extracted from the input performance. Then, develop a system that can convert this rhythm into a drum loop.
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/groove2drum.png" alt="dev_stages" style="width: 700px;"/>

<br> 

> **How to extract rhythm from live performances?**
> 
> Simply flatten all the notes into a single track, then represent similar to the drum loop representation.
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/flatten.png" alt="dev_stages" style="width: 350px;"/>

<br> 

> **Final Architecture to Train**
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/arch_aimc.jpeg" alt="dev_stages" style="width: 700px;"/>

<br> 

> **Dataset**
> 
> Ideally, we needed paired instrumental performances and drum loops.
> However, to keep it simple, we initially focused on using a drum only dataset [(Groove MIDI Dataset)](https://magenta.tensorflow.org/datasets/groove).
> As such, we trained a model that would convert a drum rhythm into a multi-voice drum pattern.
> 
> In the final real-time system, we could then replace the drum rhythm with the rhythm extracted from the live performance.
> 



> **Read More**
> 
> Details of the methodology and evaluation can be found in the following blog post I've prepared: 
> 
> [Blog Post]({{ site.baseurl }}/blog/2022/trainingGrooveTransformer/){: .btn}





<br><br><br>


---
## **2 - Creating a Real-Time Accompaniment Context Around the Loop Generator**
---

<br>

> **Main Objective**
> 
> In real-time, extract rhythms from a MIDI performance, convert into a drum loop. 
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/real-time-context-camera-ready.png" alt="dev_stages" style="width: 700px;"/>

<br>

> **Model Training Vs. Inference**
> 
> During training, convert drum groove to drum pattern. 
> 
> In real-time inference, replace drum groove with instrumental groove. 
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/pipeline_camera_ready.png" alt="dev_stages" style="width: 700px;"/>


<br>

> **Deployment**
> 
> Overdub inputs to create a longer evolving accompaniment.
> 
> A VST using a [Camomile (Pure Data)](https://github.com/pierreguillot/Camomile) front-end and a python backend was developed. 
> 
> Pd/Camomile: Visual Interface, Midi Processing, Sequence Playback, and Drum Synthesis
> 
> Python Backend: Model Inference
> 
> Communication: OSC
> 
> In real-time inference, replace drum groove with instrumental groove. 
> 
> <img src="{{ site.baseurl }}/assets/img/aimc2021/real-time-implemented_camera_ready.png" alt="dev_stages" style="width: 700px;"/>


> **Further details can be found in the following publication:**
<div class="publications"> {% bibliography -f papers -q @*[key=haki_behzad_2022_7088343]* %} </div>


<br> 

> **System Demo**
> 
> <video width="600" height="400" controls><source src="/assets/videos/RT_AIMC_trimmed.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
> <br>
> 
> <audio width="600" height="200" controls><source src="/assets/audio/AIMC_Audio_firstAccomp.mp3" type="audio/mp3">Your browser does not support the video tag.</audio>



<br><br><br>


<br><br><br>


---
## **3 - Improved Deployment Procedure**
---

- Pd/Python setup is very cumbersome. 
- Required some technical knowledge to set up the system.
- To make it more accessible, we had to develop a standalone system.
- The challenge was that there was very little resources available to develop a standalone system.
- A good deal of a year was spent on porting the system to a standalone system. 
- This was done using the [JUCE](https://juce.com/) framework as well as the [TorchScript](https://pytorch.org/tutorials/advanced/cpp_export.html) library.

> **Standalone Groove2Drum Accompaniment System**
> 
> <video width="600" height="400" controls><source src="/assets/videos/Groove2Drum.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
> <br>

[Source Code](https://github.com/behzadhaki/Groove2DrumVST){: .btn}


The development of the standalone system was a significant challenge. 
Once done, I realized that I won't be able to develop a standalone system for every upcoming project if I have to go through the same process again and again.

As such, I decided to develop a framework that would allow me to easily deploy my models in a standalone system.
This framework is called [NeuralMidiFx](https://neuralmidifx.github.io/). 
The idea behind this framework is to allow researchers to easily deploy their models in a standalone system without
having to worry about the technical details of the deployment process.

Using the framework, one can very quickly design a graphical interface using a simple JSON file. Then, all the 
communication between the interface and all the dedicated background threads in handled by the framework.

While the development of the framework was extremely costly in terms of time, it has simplified the process
to the extent that I can now develop a standalone system in a matter of days. Moreover, the framework is open-source,
and I hope that it will be useful for other researchers as well.

<br>

> **Main Idea Behind NeuralMidiFx: Division of Responsibilities**
>
> 
> <img src="{{ site.baseurl }}/assets/img/nmfx/NMFX_responsibilities.png" alt="dev_stages" style="width: 700px;"/>

<br>

> **NeuralMidiFx Architecture**
> 
> <img src="{{ site.baseurl }}/assets/img/nmfx/NMFX_Arch.png" alt="dev_stages" style="width: 700px;"/>

<br> 

> **Further details can be found in the following publication:**
<div class="publications"> {% bibliography -f papers -q @*[key=Haki2023NeuralMidiFx]* %} </div>


<br><br><br>


---
## **4 - In-Situ Evaluation of the Groove2Drum VST**
---

- The evaluation of the Groove2Drum VST was done in-situ.
- We asked [Raul Refree](https://raulrefree.com/) to come to the lab and test the system.
- Raul was asked to perform on a MIDI keyboard, and the system would generate drum accompaniments in real-time.
- Subsequently, we asked him to provide feedback on the system.

> **Feedback**
> 
> - System was hard to use at first.
> - There are many controls that are overwhelming in a live performance setting.
> - Perhaps the system was more useful in a studio/production setting.
> - If designed for live performance, it should be as autonomous as possible.
> - That said, having some quick controls to change/guide the generation process would be useful.

Following the feedback, we decided to develop a new system that would be more autonomous and would require less user input.

To do so, we modified our architecture into a Variational Autoencoder (VAE). This would allow us to generate drum loops in a more controlled manner.
That is, we could be able to guide the generation to certain predefined patterns.

This was the main focus of the `GrooveTransformer` system, discussed in the following section.

<br><br><br>

---
## **5 - GrooveTransformer**
---

- The main idea behind the `GrooveTransformer` system was to develop a system that would allow us to generate drum loops in a more controlled manner.
- i.e. allow user to fall-back to predefined patterns.
- Moreover, allow user to decide how much the generations should be guided by the input performance.

<br> 

> **Concept**
> If we develop a VAE model, then we could achieve the above objectives as follows:
> 
> <img src="{{ site.baseurl }}/assets/img/GT/latent.png" alt="dev_stages" style="width: 700px;"/>

<br>

> **Architecture**
> 
> same as before, except the variational layer.
> 
> <img src="{{ site.baseurl }}/assets/img/GT/ARCH.PNG" alt="dev_stages" style="width: 200px;"/>

<br>

> **Deployment**
> 
> The system was deployed in a standalone system using the NeuralMidiFx framework.
> 
> <video width="600" height="400" controls><source src="/assets/videos/plugin.webm" type="video/webm"> Your browser does not support the video tag. </video>
> 

<br>

> **Demos**
> 
> <video width="600" height="400" controls><source src="/assets/videos/VCV_VST_Keyboard_LowRes.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
> 
> <br>
> [More Recordings Here](https://generativedata.github.io/generated_examples/jam_session_recordings/){: .btn}

<br>


> **Refree's Live Rehearsal at CCCB**
> 
> <video width="600" height="400" controls><source src="/assets/videos/arturia.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
> 
> <br>
>  
> <video width="600" height="400" controls><source src="/assets/videos/phone.mp4" type="video/mp4"> Your browser does not support the video tag. </video>

<br><br><br>


---
## **6 - GrooveTransformer in Euro-rack Format**
---

- Main objective was to push the users to interact with the system in a context that the model was not developed for.
- i.e. use unconventional rhythms and also synthesize the drums in a more unconventional manner.

<br>

> **Final Prototype**
>
> <img src="{{ site.baseurl }}/assets/img/GT/GT_Euro_.jpg" alt="dev_stages" style="width: 700px;"/>

<br>

> **Deployment Procedure**
> 
> <img src="{{ site.baseurl }}/assets/img/GT/hardware.png" alt="dev_stages" style="width: 700px;"/>

<br>

> **Demos**
> 
> Setup:
> 
>For the GrooveTransformer’s input groove, it receives a multiple of the Intellijel Metropolix gate and pitch sequence that controls the Acid Technology Chainsaw voice in the Eurorack. **In this scenario, we have opted to use the pitch values of each note event to represent the velocity of the input**. The pitch and gate voltages are sent from the Eurorack to the GrooveTransformer via an Expert Sleepers ES-9 DC-coupled audio interface and a Cardinal CV to MIDI converter plug-in. Generated drum patterns from the GrooveTransformer are converted to Control Voltage (CV) and sent to the Eurorack via a PolyEnd Poly2 MIDI to CV converter.
> 
> Drum Synthesis:
>
> We use 7 voices of the generated patterns (kick, snare, open and closed hi-hat, and lo/mid/hi tom) to trigger 4 voices in the Eurorack:
Kick: Schlappi Engineering Angle Grinder + Make Noise Moddemix VCA + Intellijel Quadrax envelope generator Snare: Intellijel Plonk Open and Closed Hi-Hats: Basimilus Iteritas Alter Lo, Mid, Hi Toms: Akemie’s Taiko
> 
> To retain generated dynamics, the kick, hi-hats, and toms are routed to individual channels on a Mutable Instruments Veils. The level of each channel is controlled with the velocity sequence associated with the corresponding voice The Intellijel Plonk has a dedicated velocity input that we utilized rather than routing the signal to Veils
> <video width="600" height="400" controls><source src="/assets/videos/eurorackJam.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
> 

<br>

> **Further details can be found in the following publication:**
 
<div class="publications"> {% bibliography -f papers -q @*[key=Haki2024GrooveTransformer]* %} </div>



<br><br><br>

---
## **6 - Improved Controllability**
---

- Using user feedback, we decided to improve the controllability of the system.
- Added Genre control and Voice Redistribution controls:

<br>

> **Architecture**
> 
> <img src="{{ site.baseurl }}/assets/img/control_GT/control_models.png" alt="dev_stages" style="width: 700px;"/>

<br>

> **Deployment**
> 
> [Download the VST Plugin](https://generativedata.github.io/resources/source_code_and_vst_plugins/){: .btn}
> 

<br>

> **Note**
> 
> Currently, under review for ISMIR 2024. However, extra information can be found [here](https://generativedata.github.io/){: .btn}
> 

<br><br><br>
--- 
## **7 - Adaptation to Audio**
---

- The main objective was to adapt the system to audio input.
- We had done one experiment before, which used audio input with the same architecture employed for the symbolic2symbolic systems.
- Read the following publication for more details:

<div class="publications"> {% bibliography -f papers -q @*[key=Haki2023Completing]* %} </div>

> **Previous Work on Audio Input**
> 
> <img src="{{ site.baseurl }}/assets/img/audio2drum/pipeline_1.5x.png" alt="dev_stages" style="width: 700px;"/>

<br> 

- The initial idea was to use the above approach for adapting the current systems to audio input. 
- Given time constraints, we decided to use a simpler approach.
- We use a publicly available onset detection system called [DDC_Onset](https://github.com/chrisdonahue/ddc_onset) to extract onsets from the audio input.
- We then convert these onsets into a drum loop using the GrooveTransformer system.
- The system was deployed in a standalone system using the NeuralMidiFx framework.

> **Deployment**
> Developed plugins will be released soon.

<br>

> **Demos**
> 
> <video width="600" height="400" controls><source src="/assets/videos/AudioInputDemo1.mp4" type="video/mp4"> Your browser does not support the video tag. </video>
> 


<br><br><br>
--- 
## **8 - Going Beyond Drum Grooves**
---

- Objective here was to develop the system such that it had knowledge of the type of instrument being played.
- i.e. It was able to model the rhythmic interplay between different instruments and drums.
- For this, we developed a number of Groove2Groove conversion systems using the same architecture as the GrooveTransformer system.
- These systems are then paired with the GrooveTransformer system to generate drum loops that are interlocked with the input performance.
- for the data, we've used the [Lakh MIDI Dataset](https://colinraffel.com/projects/lmd/). In here, there are many multi-track midis that we can use to train the Groove2Groove systems.
- For these systems, we've focused on Bass-Drum, Guitar-Drum, and Piano-Drum pairs.

<br>

- The details of this work will be released soon.

> **Demos**
> 
> <audio width="600" height="200" controls><source src="/assets/audio/G2GTest2_June22Edit.mp3" type="audio/mp3">Your browser does not support the video tag.</audio>

