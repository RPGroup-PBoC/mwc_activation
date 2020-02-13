import sys
sys.path.insert(0, '../../../')
import numpy as np
import pandas as pd
import glob
import os
import imp
import act.flow
import tqdm

# Define the experiment parameters
DATE = '20180628'
gating_fraction = 0.4

# Make sure the outputfiles exist. 
if os.path.exists('./output') != True:
    os.mkdir('output')

# Load all files.
files = glob.glob(f'../../../data/flow/csv/{DATE}/*.csv')

for f in tqdm.tqdm(files, desc='processing flow cytometry files...'):
    # Load in the data
    data = pd.read_csv(f)
    gated_bool = act.flow.gaussian_gate(data, gating_fraction)
    gated = gated_bool[gated_bool['gate']==1].copy()
    
    # Save the gated data. 
    gated_bool.to_csv(f, index=False)
    
print('finished!')
