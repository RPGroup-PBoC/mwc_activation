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
DATE = '20190213'
RUN_NO = 1
gating_fraction = 0.4
promoter ='27yfp'

# Make sure the outputfiles exist. 
if os.path.exists('./output') != True:
    os.mkdir('output')

# Load all files.
files = glob.glob(f'../../../data/flow/csv/{DATE}_r{RUN_NO}_{promoter}*.csv')

# Set up the DataFrame
colnames = ['date', 'promoter', 'strain', 'atc_ngml', 'xan_mgml', 'mean_FITC']
df = pd.DataFrame([], columns=colnames)
for f in tqdm.tqdm(files, desc='processing flow cytometry files...'):
    # Get the identifying finformation.
    _, _, promoter, strain, atc, xan = f.split('/')[-1].split('_')
    atc = float(atc.split('ngml')[0])
    xan = float(xan.split('mgml')[0])
    
    # Load in the data
    data = pd.read_csv(f)
    gated_bool = act.flow.gaussian_gate(data, gating_fraction)
    gated = gated_bool[gated_bool['gate']==1].copy()
    
    # Save the gated data. 
    gated_bool.to_csv(f, index=False)
    
    # Compute the mean
    mean_FITC = gated['FITC-H'].mean()

    # Assemble the dictionary
    samp_dict = dict(date=DATE, promoter=promoter, strain=strain,
                     atc_ngml=atc, xan_mgml=xan, mean_FITC=mean_FITC)
    df = df.append(samp_dict, ignore_index=True)

mean_auto = np.mean(df[df['strain']=='auto']['mean_FITC'])
mean_delta = np.mean(df[df['strain']=='delta']['mean_FITC']) #- mean_auto
df['fold_change'] = (df['mean_FITC']) / mean_delta #(df['mean_FITC'] - mean_auto) / mean_delta

# Save to a CSV.
df.to_csv(f'output/{DATE}_r{RUN_NO}_{promoter}_fold_change.csv')
print('finished!')
