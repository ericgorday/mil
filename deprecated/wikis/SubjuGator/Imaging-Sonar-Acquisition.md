We needed an imaging sonar for underwater SLAM. We have purchased a Telodyne BlueView P900 and had success using it for basic object detection. This page documents the call-center style scramble that was used to find it.

# Requirements
- High update rate, so we don't have to deal with motion nonsense
    - Most 2D multibeam sonars are unaffected by motion

# Desirements
- Avoid a plane-scanning sonar, so we don't have to mechanically scan

# What we don't want
- Low quality side-scan sonar (This is for fishermen and mapping from a surface vessel)

# Products

| Name/Link  | FOV |  Range | Update Rate (Hz)  |  Communication        |  Size  | Weight  | Price  | Notes |
|-----------:|:---:|:------:|:-----------------:|:---------------------:|:------:|:-------:|:------:|:------:|
| [Teledyne M900](http://www.blueview.com/products/2d-imaging-sonar/m900-series/) | 90 deg or 130 deg | 100m  | 25Hz | Ethernet/VDSL | 19.20 x 10.16 cm x 10 cm (LxWxH) | 0.86 lbs | UNKNOWN! | |
| [Teledyne m450](http://www.blueview.com/products/2d-imaging-sonar/m450-series/) | 90 deg or 130 deg | 300m | 25Hz | Ethernet/VDSL | 22.86 x 19.56 x 10.16 cm (LxWxH) | 0.86 lbs | UNKNOWN! | |
| [M900X FLS](http://www.blueview.com/products/2d-imaging-sonar/m900xm450x-forward-looking-multibeam-imaging-sonar-solutions/) (This is the dream) | 130x20 deg (Horizontal) 45x20 deg (Vertical) | 100m | 15 Hz | Ethernet | Unlisted  | Unlisted | UNKNOWN!| This guy is exactly what we're after (The P900's would also suffice) |
| [M450X FLS](http://www.blueview.com/products/2d-imaging-sonar/m900xm450x-forward-looking-multibeam-imaging-sonar-solutions/) | 130x15 deg (Horizontal) 45x15 deg (Vertical) | 280m | 15 Hz | Ethernet | Unlisted  | Unlisted | UNKNOWN!| |
| [Sonartronic WBMS 128 FLS](http://www.sonartronic.com/pdf/WBMS-128-FLS.pdf) | 90 deg horizontal 20 deg vertical | 100m | 20 Hz | Ethernet | 6.7 x 23.1 x 15.4 cm  (HxWxD) | 1.2 kg | UNKNOWN! | |
| [Garmin Panoptix](https://buy.garmin.com/en-US/US/on-the-water/transducers/panoptix-ps30-down-transducer/prod149188.html) | 120x6 (User steerable) | 100m | Unknown, not very fast | UNKNOWN, proprietary (Probably ethernet) | Small | 1.8 lbs | $1,500 | Cheapest available sonar that will do the job. It's slow, and we'll have to reverse engineer the communication format (There is no guarantee that we will be able to do this at all) |


# Yet to be explored
* FarSounder FS-3DT and FS-3ER 3D Models
* Interphase Twinscope
* Tritech Eclipse
* BlueView P900
* Marine Electronics 6201 and SeaEcho
* Reson SeaBat 7128
* Echopilot (Gold Platinum and future 3D)
* L-3 Communication Subeye

# Links
* [Video of P900-130 view](https://www.youtube.com/watch?time_continue=8&v=pSNoFgEtook)
* [Imaging Sonars for ship operators](http://www.farsounder.com/files/NavigationSonarForTheShipOperator_ForwardLookingSonarsAndMultibeamEchosoundersExplained.pdf)


# How do we get one

* Kickstarter
* Beg university for funding (Unlikely)
* Maybe we can get an old P-Series?
    * The P900 fits our reqirements very well, but they are cancelled
    * There may be a lab at UF or elsewhere in Florida that is no longer using theirs
* Researchers at UF? Mohseni?
    * Prove that we can do SLAM with the Velodyne
    * Or do Monocular SLAM
* Some of the older models suit us well, we should contact labs, government agencies and companies that may have old ones
* Just buy one if it's under $3000

# Notes
* Underwater SLAM for robots is not very common...people do obstacle avoidance, but not much in the way of true SLAM
    * There is a book called "Underwater SLAM in structured environments using an imaging sonar"

# Need to call
* Teledyne
* VideoRay
* RayMarine
* Halliburton
* BlueFin
* Transocean
* Gemini (UK)
* Sonartronic (Denmark)

# Other options
- [Structured Light Sensor](http://dspace.mit.edu/bitstream/handle/1721.1/83705/864435344-MIT.pdf)
- We can get our own Pico projector dev kit [here](http://www.ti.com/tool/dlp1picokit)
    - Do we have friends at TI who can help us get ahold of one of these?
    - If not, let's just do it with a scattering laser diode


# So what's the plan?
Find a good sonar. Call the company, and prove to them that we can make *them* the face of underwater SLAM.