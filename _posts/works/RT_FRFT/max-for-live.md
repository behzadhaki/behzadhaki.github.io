
## MaxForLive Integration

All of the above methods have also been implemented as Max for Live devices that can be used within Ableton Live.

<img src="/assets/works/RT_FRFT/m4l-devices.png" alt="Description" width="100%">

{: .note }
These devices are accessible in the `Max 8 (or 9)/Packages/FRFT/m4l` folder after installation:
- `alpha-synth&processor.amxd`
- `alpha-convolution.amxd`
- `alpha-filter.amxd`
- `alpha-RM.amxd`
- `alpha-feedback.amxd`

The underlying FRFT operations in these devices are the same as in the standalone Max patches. 
The main difference is the Max for Live interface, which allows for easier integration into Ableton Live 
projects and provides a more user-friendly control surface for the parameters.

## Overview of Interface  

<br>

**Windowing and Mix Controls (available in all devices)**

<img src="/assets/works/RT_FRFT/windowing-mixer.png" alt="Description" width="40%">

**Input Audio Routing (available in all devices)**

Depending on the device, one or two audio inputs are required for the processing. These sources can be set via the `A`/`B` panels.

The audio can come either from the track on which the device is loaded (called 'internal' source) or from a built-in oscillator (called 'osc'):

<img src="/assets/works/RT_FRFT/audio-source-int-osc.png" alt="Description" width="40%">

Moreover, in the case of α-convolution and α-RM devices, the second source can also be routed from anywhere in the Live set using the 'external' option:

<img src="/assets/works/RT_FRFT/audio-source-ext.png" alt="Description" width="40%">

**$\alpha$ Control Panels**

For controlling the α parameters, we have implemented a custom control interface that allows for high-precision adjustments to the α values in real-time.

Instead of specifying a single α value, the user can specify a range of allowed α values (by setting the center and width of the range), and then a dedicated slider is used to smoothly navigate within that range.

<img src="/assets/works/RT_FRFT/alpha-control.png" alt="Description" width="40%">

In the case of α-RM, where we have two independent α parameters, the interface allows for controlling the ranges of both parameters independently or linking the second parameter to the first one with a specified offset (e.g. $\alpha_2 = \alpha_1 + 1.0$)

<img src="/assets/works/RT_FRFT/alpha-control-RM.png" alt="Description" width="40%">


**Feedback and Filter Controls**

In the α-feedback and α-filter devices, we have a panel for controlling the filter parameters:

Moreover, in the α-feedback device, we have a dedicated panel for controlling the feedback amount:

<img src="/assets/works/RT_FRFT/filter-feedback-control.png" alt="Description" width="40%">
