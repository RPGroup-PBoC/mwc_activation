---
status: rejected
reason: Experiment not yet completed
---

# 2019-02-19 (RUN 1) Xanthosine Titration

## Purpose: Replicate run of xanthosine titration series 
This experiment serves as a replicate of a xanthosine titration across a wide
range of concentrations of xanthosine. 

## Strains
| **Location** | **Plasmid** | **Genotype** | **Shorthand** |
|:--| :--| :--| :--| 
|`Box 1-17`| `N/A`| *xapABR::FRT-FRT* | `auto`|
|`Box 1-18`| `N/A`| *galK::27-YFP, xapABR::FRT-FRT* | `∆xap`|
|`Box 1-27`| *pN25-tetR*| *ybcN::1-xapR-mCherry, galK::27-YFP, xapABR::FRT-FRT*| `27yfp`|

## Inducer concentrations
| **Inducer** | **Shorthand**| **Concentration(s)** |
|:--|:--| :--|
| Anhydrous tetracycline| ATC| 10 \[ng/mL\]|
| Xanthosine dihydrate | XAN | 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5, 4, 5, 6, 8, 10, 15, 20 \[mg/mL\]|

## Notes & Observations
To XAN concentrations 0 - 3.5, I initially added 30 µL of 100 ng /mL ATC
stock rather than 1µg/mL. I neglected the added xanthosine and added another
30 µL of 1 µg/mL.

## Processing Files

### Cell Husbandry
1. All strains given in the table above were grown in LB + appropriate
   antibiotic overnight (reaching saturation) and were in stationary phase. 
2. The previous night, the appropriate amount of Xanthosine was weighed into the
  appropriate 15 mL Falcon tubes.
3. The following morning, 3 mL of M9 + 0.5% glucose was added to each tube (±
   xanthosine) followed by the appropriate antibiotic (if necessary) and
   concentration of ATC. ATC was diluted from 1µg/mL stock. Xanthosine was
   prepared as a 20 mg/mL stock by heating the growth media in the microwave and
   dissolving the weighed powered xanthosine. Dilutions to the other
   concentrations were made from this stock. 
4. Cells were diluted 1000 fold into the media and allowed to grow for ~ 8 hours
   shaking 225 rpm at 37°C. The tubes were shielded from light to prevent
   photocleavage of the ATC. 
5. After 8 hours, the cultures were removed from incubation and prepared for
  flow cytometry.

## Flow Cytometry
1. Cells were diluted 1:10 into M9 minimal medium with no supplemented carbon to
  suppress growth and further expression. 
2. Cells were flowed at medium speed with gentle mixing. The voltage settings
   were as follows:

   | Channel | Voltage |
   |:--:|:--:|
   | FSC | 433 V|
   | SSC | 537 V|
   | B1 | 574 V|

3. Once the flow was completed, data was transferred to local machine, renamed,
   and backed up to the storage server. 



