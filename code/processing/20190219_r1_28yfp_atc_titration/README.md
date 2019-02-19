---
status: Rejected 
reason: experiment not yet completed
---

# 2019-02-19 28-YFP ATC Titration

## Purpose
This experiment is the flagship ATC titration of the simple-activation motif
with and without added xanthosine. 

## Strains
| **Location** | **Plasmid** | **Genotype** | **Shorthand** |
|:--| :--| :--| :--| 
|`Box 1-17`| `N/A`| *xapABR::FRT-FRT* | `auto`|
|`Box 1-24`| `N/A`| *galK::28-YFP, xapABR::FRT-FRT* | `∆xap`|
|`Box 1-28`| *pN25-tetR*| *ybcN::1-xapR-mCherry, galK::28-YFP, xapABR::FRT-FRT*| `28yfp`|

## Inducer concentrations
| **Inducer** | **Shorthand**| **Concentration(s)** |
|:--|:--| :--|
| Anhydrous tetracycline| ATC| 0, 0.1, 0.5, 1, 1.5, 2, 2.5, 5, 10 \[ng/mL\]|
| Xanthosine dihydrate | XAN | 0, 4 \[mg/mL\]|

## Notes & Observations
 
## Analysis Files

## Experimental Protocol

1. Cells as described in "Strain Information" were grown to saturation in 3mL of LB Miller (+ chloramphenicol for the `dilution` strain).

2. Cells were diluted 1:1000 into 3mL of growth media (+ chloramphenicol for the `28yfp` strain) in 14mL Falcon tubes. ATC was added from 1µg/mL stock in 50% EtOH to the appropriate concentration.

3. Tubes were placed in a rack and covered with a plastic box to protect from photocleavage of ATC. Cells were allowed to grow for X hours at 37°C with shaking at ~ 220 RPM.

4. Once the cells reached an OD<sub>600nm</sub> between 0.2 - 0.4, the cells were removed from the warm room and harvested.

**Sample OD<sub>600nm</sub> Measurements**

| Strain | ATC Concentration [ng / mL] | OD<sub>600nm</sub> |
| :--- | :---: | :---: |
| `autofluorescence` | 0 |  |
| `delta` | 0 |  |
| `28yfp` | 0.1 |  |
| `28yfp` | 0.2 |  |
| `28yfp` | 0.3 |  |
| `28yfp` | 0.4 |  |
| `28yfp` | 0.7 |  |
| `28yfp` | 1 |  |
| `28yfp` | 10 |  |

**Microscopy**

1. A 100µL aliquot of each of the `dilution` samples with varying ATC concentrations were combined in a 1.5mL eppendorf tube.

2. This `dilution` mixture was pelleted at 13000xg for 2 min. The supernatant was withdrawn and the pellet was resuspended in 1mL of ATC-free growth medium. This procedure was repeated twice more.

3. The washed `dilution` mixture was diluted 1:10 into ATC-free growth medium. Aliquots of 1µL were spotted onto 3% agarose pads made of the growth medium.

4. The other samples (`autofluorescence`, `deltaLacI`, and `dilution` for all ATC concentrations except 10ng/mL) were diluted 1:5 into a growth medium with no available carbon. Aliquots of 1µL were added to agarose pads made of the growth medium with no added carbon.

5. Agarose pads spotted with cells were allowed to dry and were then placed onto a glass bottom dish.

6. After mounting, the sample dish was affixed to the microscope using double stick tape. Between five and ten positions were marked per snapshot sample. Exposures were as follows:
    - Brightfield - 100ms, gain 4, 12bit
    - mCherry - 500ms, gain 4, 12bit
    - YFP - 500ms, gain 4, 12bit

7. Approximately 15 positions were then marked on the `dilution` mixture pad. These positions were chosen requiring separation of cells and avoidance of debris.

8. These were positions were imaged every 7 minutes for 1.5 hours using only the Brightfield channel. After this timelapse, these positions were imaged once more using Brightfield, mCherry, and YFP channels.

9. The samples were discarded and the dataset was transferred to the storage server.