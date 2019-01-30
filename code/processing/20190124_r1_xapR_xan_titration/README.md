---
status: rejected
reason:
    This experiment screens through strains generated for the project and
    ensures that they work appropriately. These data should not be included into the
    formal processing and analysis steps.
---

# 2019-01-24 Strain Screening

## Purpose 
In this experiment, strains used for the dilution experiments are tested across
two ATC and Xanthosine concentrations. The highest xanthosine concentration was
chosen to target the bimodal distribution observed at MBL 2018.

## Strains
| **Location** | **Plasmid** | **Genotype** | **Shorthand** |
|:--| :--| :--| :--| 
|`Box 1-17`| `N/A`| *xapABR::FRT-FRT* | `∆xap`|
|`Box 1-24`| `N/A`| *galK::28-YFP, xapABR::FRT-FRT* |`simp-YFP`|
|`Box 1-18`| `N/A`| *galK::27-YFP, xapABR::FRT-FRT* | `wt-YFP`|
|`Box 1-28`| *pN25-tetR*| *ybcN::1-xapR-mCherry, galK::28-YFP, xapABR::FRT-FRT*| `simp-YFP + xapR`|
|`Box 1-27`| *pN25-tetR*| *ybcN::1-xapR-mCherry, galK::27-YFP, xapABR::FRT-FRT*| `wt-YFP + xapR`|

## Inducer concentrations
| **Inducer** | **Shorthand**| **Concentration(s)** |
|:--|:--| :--|
| Anhydrous tetracycline| ATC| 0, (0.5, 1, 5), 10 \[ng/mL\]|
| Xanthosine dihydrate | XAN | 0, 5 \[mg/mL\]|

## Processing Files


## Protocol
### Cell Husbandry
1. All strains given in the table above were grown in LB + appropriate
   antibiotic overnight (reaching saturation) and were in stationary phase. 
2. The previous night, the appropriate amount of Xanthosine was weighed into the
  appropriate 15 mL Falcon tubes.
3. The following morning, 3 mL of M9 + 0.5% glucose was added to each tube (±
   xanthosine) followed by the appropriate antibiotic (if necessary) and
   concentration of ATC. ATC was diluted from 1µg/mL stock. 
4. Cells were diluted 1000 fold into the media and allowed to grow for ~ 8 hours
   shaking 225 rpm at 37°C. The tubes were shielded from light to prevent
   photocleavage of the ATC. 
5. After 8 hours, the cultures were removed from incubation and prepared for
   imaging. 
6. Agarose pads containing M9 minimal medium with no carbon and M9 + 0.5%
   glucose were prepared by microwaving 5mL of the solvent with 0.1 - 0.15 g of
   ultrapure high melting temperature agarose until molten. 
7. 300 - 500 µL of each molten agarose mixture was pipetted onto glass slides
   and allowed to cool to room temperature and were then cut into ~1 cm^2^ pads. 
8. While the pads were cooling, the cells were prepared for imaging. 150 µL of
   the `simp-YFP + xapR` culture grown in 0.5, 1, 5, and 10 ng/mL of ATC were
   combined into a single tube and spun at 13000 rpm for 1 min. 
9. The supernatant was removed and replaced with 1 mL of M9 + 0.5% glucose
   without ATC. The cells were then spun again at 13000 rpm for 1 minute. This
   process was repeated two more times for a total of 3 volume exchanges. 
10. The mixture sample was diluted 5 fold into M9 + 0.5% glucose. A 1 µL aliquot
    was added to one of the M9 + 0.5% glucose + 2% agarose pad and was spread
    using a loop. 
11. The remaining cultures were diluted 1:10 into M9 minimal medium without
    carbon and vortexed. A 1µL aliquot was then transferred to an agarose pad
    made from M9 minimal medium without carbon. 
12. Agarose pads were allowed to dry for 5 - 10 min and were then inverted onto
    a glass bottom dish. The dish was sealed with parafilm and double-sticky
    tape was affixed to the sides of the bottom surface of the dish to affix the
    sample to the microscope.   

### Microscopy 
1. The imaging dish was affixed to the stage and was allowed to equilibrate to
   the incubation chamber for 10 min while microscope parameters were set. 
2. The different promoters have different levels of YFP expression, meaning that
   the exposure and gain settings had to be reset between the two promoter
   samples. The exposure times and camera settings were as follows:

   | **Channel** | **Promoter** |**Exposure (ms)** | **Bit-depth & Gain**|
   |:--|:--|:--| :--|
   |Brightfield | `simp-YFP` & `wt-YFP`| 100 | 12-bit & Gain 1|
   |YFP | `simp-YFP` | 500 | 12-bit & Gain 4 |
   | YFP | `wt-YFP` | 400 | 12-bit & Gain 1 |
   |mCherry | `simp-YFP` & `wt-YFP` | 500 | 12-bit & Gain 4|

3. Between 10 - 15 positions were marked per sample pad and images were
   acquired. Positions were chosen to be at least 1.5 FOV's apart from each
   other to avoid double exposure of cells. 

4. Once the snapshots had been acquired, the growth movie of mixed & washed
   `simp-YFP + xapR` culture was acquired as an ND-sequence acquisition. The
   acquisition was taken in two phases. The first was a phase-contrast time
   series with images taken every 7 min for 1.5 hrs (13 loops). Once completed, 
   a final round in phase contrast and mCherry was acquired for every position
   following the exposures and gain settings described in the table above.
5. Once completed, images were manually exported to `.tif` files and transferred
   to the data storage server and computational machine for processing.  