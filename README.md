[![Build Status](https://travis-ci.org/RPGroup-PBoC/mwc_activation.svg?branch=master)](https://travis-ci.org/RPGroup-PBoC/mwc_activation)
# Quantitative Dissection of the Simple Activation Motif

## Overview
This repository contains all experimental and theoretical details for the MWC
activation project.


## Layout
The repository is split into seven main directories, many of which have
subdirectories.Each section is briefly described below.

### **`code`** 
Where all of the *executed* code lives. This includes pipelines, scripts, and figure files. 
 * **`processing`**: All code to process raw data files and generate `.csv`
   files for analysis.
 * **`analysis`**: All executed code used to perform statistical and physical
   analysis. 
 * **`stan`**: All statistical models written in the `Stan` programming language.
 * **`sandbox`**: All exploratory code from analysis to processing.
 * **`figures`**: All code used to generate figures for presentations,
   documents, and summaries.

### **`data`** 
All processed data files. Untracked large data sets are stored locally here. 

### **`miscellaneous`** 
Files that may not be code, but are important for reproducibility.
* **`protocols`**: A well annotated and general description of experiments.
* **`materials`**: Information regarding the materials, primers, and strains
  used in experiment.
* **`software details`**: Information about your computational environment that are necessary for others to execute your code. This includes details about your operating system, software version and required packages.

### **`tests`** 
All test suites for the `act` module.

### **`act`** 
Python software module used in processing and analysis.

### **`templates`** 
Blank templates that document the procedures taken for each experiment, simulation, or analysis routine. 

### **`doc`**
All `.tex` and `.md` files used for write ups, summaries, and manuscripts. 

## Other important files
1. **`LICENSE`**: A copy of the MIT license for all software unless otherwise stated. 

2. **`README.md`**: This document. 


# License Information
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"></a>.
All creative work is licensed under a [CC-BY
4.0](http://creativecommons.org/licenses/by/4.0/) license which permits copying
and redistribution in any medium or format as well as transformation, remixing,
and commercial use of this material. Proper attribution to the authors is required for *any* use
of this material. 

All software written by the authors is licensed under a standard MIT license
which reads as follows: 

```
MIT License

Copyright (c) Griffin Chure, Nathan Belliveau, Rob Phillips 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```