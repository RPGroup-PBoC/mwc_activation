#%% 
import numpy as np
import fcsparser
import os
import glob

# Define the details fo the expriment.
DATE = ''
atc_conc =  # in ng/mL
RUN_NO = 
promoter = ''

## Hardcoded arrangement garbage. 
xan_mgml = [0, 0, 0, 0.1, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 10]
_strains =  ['auto', 'delta', ['dilution'] * len(xan_mgml)]
strains =  [l[i] for l in _strains for i in range(len(l))]

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
