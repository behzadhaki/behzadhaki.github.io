
## Source Code

<div class="proj-btn-row">
<a class="proj-btn proj-btn--download" href="https://groovetransformer.github.io/assets/zip/DaisySeedCode.zip" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> Daisy Seed Source (C++)</a>
<a class="proj-btn proj-btn--download" href="https://groovetransformer.github.io/assets/zip/LibreBoardCode.zip" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> Libre / RPi Code (Python)</a>
<a class="proj-btn proj-btn--download" href="/assets/works/GrooveTransformerEurorack/AdditionalNotes.pdf" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> Additional Notes (.pdf)</a>
</div>

## PCB

### Production Resources

<div class="proj-btn-row">
<a class="proj-btn proj-btn--download" href="/assets/works/GrooveTransformerEurorack/Schematic_FrontPCB.pdf" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> Front PCB Schematic (.pdf)</a>
<a class="proj-btn proj-btn--download" href="/assets/works/GrooveTransformerEurorack/Schematic_BottomPCB.pdf" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> Bottom PCB Schematic (.pdf)</a>
<a class="proj-btn proj-btn--download" href="https://groovetransformer.github.io/assets/zip/PCB_Gerber_Files.zip" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> PCB Gerber Files (.zip)</a>
<a class="proj-btn proj-btn--download" href="https://groovetransformer.github.io/assets/zip/JLCPCB_Production_Files.zip" target="_blank" rel="noopener"><span class="proj-btn__badge"><i class="fa-solid fa-download"></i></span> JLCPCB Production Files (.zip)</a>
</div>

### Images

<img src="/assets/works/GrooveTransformerEurorack/pcb/BackPCB.png" alt="BackPCP 1" style="width: 25%;">
<img src="/assets/works/GrooveTransformerEurorack/pcb/BackPCB2.png" alt="BackPCP 2" style="width: 25%;">

<img src="/assets/works/GrooveTransformerEurorack/pcb/FrontPCB.png" alt="FrontPCP 1" style="width: 25%;">
<img src="/assets/works/GrooveTransformerEurorack/pcb/FrontPCB2.png" alt="FrontPCP 2" style="width: 25%;">

## Faceplate

### Design

<img src="/assets/works/GrooveTransformerEurorack/pcb/Panel Design.jpg" alt="Panel Design" style="width: 25%;">

### Different Finishes

`No Faceplate:`

<img src="/assets/works/GrooveTransformerEurorack/faceplate/NoFaceplate.jpg" alt="NoFaceplate" style="width: 25%;">

`Laser Cut and Laser Etched Wood:`

<img src="/assets/works/GrooveTransformerEurorack/faceplate/Wood.jpg" alt="Wood" style="width: 25%;">

`Glass:`

<img src="/assets/works/GrooveTransformerEurorack/faceplate/Glass.jpg" alt="Glass" style="width: 25%;">

`Glass with Printed Sticker:`

<img src="/assets/works/GrooveTransformerEurorack/faceplate/print_.jpg" alt="Sticker" style="width: 25%;">

## Interface Controls and Parameters

|                                    | Figure Index | Name                         | Description                                                                                                                               |
|------------------------------------|--------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Utility Parameters**             | 1            | Internal Clock Tempo Knob    | Sets the internal clock tempo                                                                                                             |
|                                    | 2            | Internal Clock CV Output     | CV clock output                                                                                                                           |
|                                    | 3            | External Clock CV Input      | Input for external CV clock source                                                                                                        |
|                                    | 4            | Metronome Click Output       | Metronome click audio output                                                                                                              |
|                                    | 5            | Play/Stop Switch             | Starts and stops the outputs and input groove record buffer                                                                               |
|                                    | 6            | Record/Overdub/Off Switch    | Three-way switch to change the mode of the input groove record buffer                                                                     |
|                                    | 7            | Clear Button                 | Clears the input groove record buffer                                                                                                     |
|                                    | 8            | Shift Button                 | Enables secondary functions of other buttons                                                                                              |
| **CV/MIDI Pattern Generation Output** | 9        | CV Gate Voice Output         | MIDI output and CV gate and velocity output for each voice                                                                                |
|                                    | 10           | CV Velocity Voice Output     |                                                                                                                                           |
|                                    | 11           | MIDI Output                  |                                                                                                                                           |
| **Input Groove Control**           | 12           | Input Groove CV Gate Input   | MIDI input and CV gate and velocity input for input groove                                                                                |
|                                    | 13           | Input Groove CV Velocity Input |                                                                                                                                         |
|                                    | 14           | Input Groove MIDI Input      |                                                                                                                                           |
|                                    | 15           | Input Groove Velocity Knob   | Quantizes the input groove to the grid and quantizes the velocity of each note                                                            |
|                                    | 16           | Input Groove Offset Knob     |                                                                                                                                           |
| **Generation Control**             | 17           | Uncertainty Knob             | Sets the value of the Uncertainty parameter                                                                                               |
|                                    | 18           | Uncertainty CV Input         | CV input for the Uncertainty parameter                                                                                                    |
|                                    | 19           | Voice Density Knob           | Controls the number of hits in each sequence by adjusting the threshold of the model                                                      |
|                                    | 20           | Voice Velocity Scale Knob    | Scales the velocity output. At minimum value, no scaling is applied to the outputs. At maximum value, all velocities are scaled to the maximum value. |
| **Latent Space Interpolation**     | 21           | Preset Selection Knob        | Selects the preset number to be loaded or to be saved to. A preset consists of the saved states in the latent space Z_A and Z_B         |
|                                    | 22           | Preset Save/Load Button      | Saves current states Z_A and Z_B to the selected preset number. Pressing with shift button loads the preset at the selected preset number |
|                                    | 23           | Save/Randomize A and B Button | Sets the current state to be Z_A or Z_B in the latent space. Pressing with shift button generates a random placement for Z_A or Z_B in the latent space |
|                                    | 24           | A/B Interpolation Slider     | Interpolation position \( \alpha \) between states Z_A and Z_B in the latent space                                                        |
|                                    | 25           | A/B Interpolation CV Input   | CV input to automate the interpolation position \( \alpha \) in the latent space                                                          |
|                                    | 26           | Follow Knob                  | Sets the value of the Follow parameter \( \beta \) in the latent space                                                                    |
|                                    | 27           | Follow CV Input              | CV input to automate the Follow parameter \( \beta \)                                                                                     |
