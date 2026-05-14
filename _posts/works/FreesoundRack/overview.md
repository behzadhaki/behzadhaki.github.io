
## What is Freesound Rack?

`Freesound Rack` is a VST/AU/Standalone plugin that allows users to search, preview, and load sounds from the Freesound database directly into their Digital Audio Workstation (DAW) or audio software. 

It provides a convenient way to access a vast library of sounds available on Freesound without needing to access the Freesound website or download sounds manually.

{: .note}
This is the very early stages of the development of this plugin. I've been working on this project in my spare time in the past month and have many features planned for the future.
That said, even at this early stage, I believe it can be useful for users to quickly explore Freesound resources. 
Unfortunately, right now, the plugin is only available for macOS, but I've been working on making it available for Windows and Linux as well.

At the core of the app is a 4x4 grid of slots, each of which can be used to search for and load a sound from Freesound.
These sounds can then be triggered manually via your keyboard, or your mouse, or via MIDI input. 

<img src="/assets/works/FreesoundRack/FreesoundRack.gif" alt="Thumbnail" width="80%">


## Quick Guide 

To make a query, simply write a search term in the search box at the bottom of each slot and press the "Search" icon (magnifying glass).

This will select a random sound matching your query and load it into the slot. You can replace the sound in a slot by making a new search.

<img src="/assets/works/FreesoundRack/quick_guides.001.png" alt="Thumbnail" width="80%">

Alternatively, you can populate multiple pads at once using the search panel at the bottom of the plugin.

To do so, from the 4x4 grid of buttons on the bottom-left, decides which pads are to be populated at once. Then, 
use the search box to write your query and press the "Search Selected" button.

<img src="/assets/works/FreesoundRack/quick_guides.002.png" alt="Thumbnail" width="80%">

Each pad has a few attributes. You can easily re-position/re-populate the pads by dragging and dropping them to a new position.
Moreover, metadata of the sample are quickly accessible from the pad itself, without requiring to finding the sound on Freesound.

<img src="/assets/works/FreesoundRack/quick_guides.003.png" alt="Thumbnail" width="80%">

Once you have populated the pads with sounds, you can create presets using the collapsable panel on the left side of the plugin.

<img src="/assets/works/FreesoundRack/quick_guides.004.png" alt="Thumbnail" width="80%">

Any sound downloaded from freesound is stored locally, even if you decide not to use it in any of your presets/projects. 
These sounds as well as your bookmarked sounds can be accessed from the "Sample Browser" panel on the right side of the plugin.

<img src="/assets/works/FreesoundRack/quick_guides.005.png" alt="Thumbnail" width="80%">

The plugin can work on its own or you can use it to find samples and load them into your DAW or audio software of choice.
Remember that you can drag the entire grid (using "All Samples" button on top left of the grid) or individual samples from the grid to your DAW.

<img src="/assets/works/FreesoundRack/FreesoundRack_dragout.gif" alt="Thumbnail" width="80%">



{: .note}
At this point, the plugin only works with preview sounds, which are lower quality versions of the original sounds. Moreover, the duration of the retrieved sounds is limited at the moment.
In the next iterations, I plan to add support for downloading and using the original high-quality sounds, as well as allowing for customizable duration for the retrieved sounds.

{: .note}
I'm also working on another application which allows to quickly access your Freesound account. The idea is to develop a number of tools that can allow for quick and easy access to Freesound resources.
The plan is to develop all these tools in a way that they can all work together and share resources. 