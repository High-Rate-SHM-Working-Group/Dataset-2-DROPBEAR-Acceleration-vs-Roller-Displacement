# Dataset-2 DROPBEAR Acceleration vs Roller Displacement (deprecated)

---
**NOTE**

This dataset is deprecated. It is recommended to use Dataset-8 "DROPBEAR-Acceleration-vs-Roller-Displacement" <a href="https://github.com/High-Rate-SHM-Working-Group/Dataset-8-DROPBEAR-Acceleration-vs-Roller-Displacement">here</a> which contains similar data but in greater quantity and quality. 
---



This data set consists of acceleration data measured from the Reproduction of Projectiles in Ballistic Environments for Advanced Research (DROPBEAR) experimental testbed with movable roller support as shown in Figure 1. DROPBEAR consists of a 51 x 6 x 350 mm beam with a single accelerometer (model 393B04 manufactured by PCB Piezotronics) mounted at the free edge of the beam. A video of the test alone can be found <a href="https://www.youtube.com/watch?v=ZB6AUWgWyJU&ab_channel=ARTS-LabattheUniversityofSouthCarolinaARTS-LabattheUniversityofSouthCarolina">here</a>.

<p align="center">
<a href="https://www.youtube.com/watch?v=ZB6AUWgWyJU&ab_channel=ARTS-LabattheUniversityofSouthCarolinaARTS-LabattheUniversityofSouthCarolina"><img src="images/DROPBEAR.png" alt="Shock test impact testing" width="800"></a>  
</p>
<p align="center">
Figure 1: The Dynamic Reproduction of Projectiles in Ballistic Environments for Advanced Research (DROPBEAR) experimental testbed with key components annotated (click the image to view the video on YouTube). 
</p>

The roller followed a predefined profile that ranged from 48 mm (closest to the fixity) to 175 mm as presented in the inset of Figure 2. The beam is self-excited by the roller's movements and therefore no extraneous inputs are required, however, this does require an initial input to the beam, which consists of a small roller movement, to initiate vibrations in the beam. In addition to this initial input, the test profile consists of six square wave inputs of increasing amplitude in addition to six sinusoidal inputs and six impulse inputs. For the cases of the square and impulse inputs, the actuator velocity was maximized to the extent allowed by the actuator and associated controller (250 mm/s). The measured vibration data is shown in Figure 3.

<p align="center">
<img src="images/pin_locatoin_data.png" alt="drawing" width="600"/>
</p>
<p align="center">
Figure 2: Displacement of roller used in the generation of this dataset. 
</p>

The measured vibration data is shown in Figure 3.  Data acquisition was performed using a 14-bit ADC (PXI-6133) for the linear transducer (SPS-L225-HALS manufactured by Honeywell) while acceleration data was acquired using a 24-bit IEPE ADC (NI-9234).

<p align="center">
<img src="images/acceleration_data.png" alt="drawing" width="600"/>
</p>
<p align="center">
Figure 3: Measured acceleration data for this data set. 
</p>

<p align="center">
<img src="images/DROPBEAR_Setup.png" alt="drawing" width="600"/>
</p>
<p align="center">
Figure 4: DROPBEAR test setup with displacement input and measured acceleration.
</p>

This data set originally published in Downey et al. "Millisecond Model Updating for Structures Experiencing Unmodeled High-rate Dynamic Events." Mechanical Systems and Signal Processing, vol. 138, 2020, p. 106551, doi:10.1016/j.ymssp.2019.106551. Published as (Distribution A. Approved for public release; distribution unlimited (96TW-2019-0372).


## Notes

This data set has subsequently been used in the following publications:
1. Austin Downey, Jonathan Hong, Jacob Dodson, Michael Carroll, and James Scheppegrell, "Millisecond Model Updating for Structures Experiencing Unmodeled High-rate Dynamic Events." Mechanical Systems and Signal Processing, vol. 138, 2020, p. 106551, doi:10.1016/j.ymssp.2019.106551.

1. Seong Hyeon Hong, Claire Drnek, Austin Downey, Yi Wang, Jacob Dodson, and Jonathan Hong., "Real-time Model Updating Algorithm for Structures Experiencing High-rate Dynamic Events." Proceedings of the ASME 2020 Conference on Smart Materials, Adaptive Structures and Intelligent Systems (SMASIS 2020), 2020, doi:10.1115/smasis2020-2439

1. Claire Rae Drnek, "Local Eigenvalue Modification Procedure for Real-time Model Updating of Structures Experiencing High-rate Dynamic Events." University of South Carolina, 2020, University of South Carolina Graduate Theses and Dissertations.


## Licensing and Citation

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Where applicable and legal, this work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa]. This license is not intended to supersede government license requirements. In good faith, all images within the repository are assumed to be licensed under a cc-by-sa [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].
 

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Cite this data as: 

Austin Downey, Jonathan Hong, Jacob Dodson, Michael Carroll, and James Scheppegrell, “Dataset-2-dropbearacceleration-vs-roller-displacement,” Dec. 2021. [Online]. Available: https://github.com/High-Rate-SHM-Working-Group/Dataset-2-DROPBEAR-Acceleration-vs-Roller-Displacement

@Misc{Downey2021Dataset2Dropbear,  
  author = {Austin Downey and Jonathan Hong and Jacob Dodson and Michael Carroll and James Scheppegrell},  
  month  = apr,  
  title  = {Dataset-2 DROPBEAR Acceleration vs Roller Displacement},  
  year   = {2020},  
  groups = {High-Rate-SHM-Working-Group},  
  url    = {https://github.com/High-Rate-SHM-Working-Group/Dataset-2-DROPBEAR-Acceleration-vs-Roller-Displacement},  
}  










