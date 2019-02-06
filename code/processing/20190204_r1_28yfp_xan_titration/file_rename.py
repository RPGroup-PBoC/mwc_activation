#%% 
import numpy as np
import fcsparser
import os
import glob

# Define the details fo the expriment.
DATE = '20190204'
atc_conc = 10 # in ng/mL
RUN_NO = 1
promoter = '28yfp'
gating_fraction = 0.4

## Hardcoded arrangement garbage. 
xan_mgml = [0, 0, 0, 0.05, 0.1, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 3.5, 4]
_strains = [['auto'], ['delta'], ['dilution'] * 13] 
strains = [l[i] for l in _strains for i in range(len(l))]

# Define directories and search pattern
src = '../../../data/flow/fcs/'
dst = '../../../data/flow/csv/'
pattern = f'RP{DATE[:4]}-{DATE[4:6]}-{DATE[6:]}_r{RUN_NO}'

# Get the names of the files.
files = np.sort(glob.glob(f'{src}{pattern}*.fcs'))

# %%Iterate through each strain and concentration. 
for s, c, f in zip(strains, xan_mgml, files):
    # Define the new name. 
    new_name = f'{DATE}_r{RUN_NO}_{promoter}_{s}_{atc_conc}ngmlATC_{c}mgmlXAN'
    
    # Load the data using fcs parser and save to csv. 
    _, data = fcsparser.parse(f)
    data.to_csv(f'{dst}{new_name}.csv')
    
    # Rename the FCS file. 
    os.rename(f, f'{src}{new_name}.fcs')
