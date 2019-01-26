# -*- coding: utf-8 -*-
# TODO:This file needs to be created into a template when a standard
# experimental procedure is set.
import sys
sys.path.insert(0,'../../../')
import glob
import os
import numpy as np 
import pandas as pd
import tqdm
import act.io
import act.bayes
import act.process

# Define experimental constants. 
DATE = 20190124
BASENAME = 'xapR_titration'
IP_DIST = 0.065

# Make the output dir if needed. 
if os.path.isdir('output') == False:
    os.mkdir('output')

# Define the data directory 
data_dir = f'../../../data/images/{DATE}_{BASENAME}/'

# ##############################################################################
# DILUTION MOVIE PROCESSING
# ##############################################################################

# Parse the clists. 
growth_clists = glob.glob(f'{data_dir}growth/xy*/clist.mat')
growth_df = act.process.parse_clists(growth_clists)

# Pass through morphological filter
growth_df = act.process.morphological_filter(growth_df, ip_dist=IP_DIST)

# Remove segmentation errors
growth_df['valid'] = growth_df['error_frame'].isnull()
growth_df = growth_df[growth_df['valid']==True]


# Note that in this experiment, all mCherry images were taken with the same 
# camera settings, so either autofluorescence sample works.
auto_samples = act.process.parse_clists(
    glob.glob(f'{data_dir}wtyfp_snaps/auto_00ngml_00mgml/xy*/clist.mat'))
auto_df = act.process.morphological_filter(auto_samples, ip_dist=IP_DIST)

# Compute the mean autofluorescence. 
mean_auto = auto_df['fluor2_mean_death'].mean()

# Compute the fluctuations. 
family_df = act.process.family_reunion(growth_df, fluo_channel=1)

# Insert identifying information. 
family_df['date'] = DATE
family_df['autofluorescence'] = mean_auto

# Compute the total fluorescence of daughters. 
family_df['I_1_tot'] = (family_df['I_1'] - family_df['autofluorescence']) * family_df['area_1']
family_df['I_2_tot'] = (family_df['I_2'] - family_df['autofluorescence']) * family_df['area_2']

# Drop cells without observed fluorescence. 
family_df = family_df[(family_df['I_1_tot'] >=0) & (family_df['I_2_tot'] >= 0)]

# Save the family dataframe to disk. 
family_df.to_csv(f'output/{DATE}_lineages.csv', index=False)

# ##############################################################################
# SNAPS PROCESSING
# ##############################################################################
snap_dfs = []
promoter_dict = {'wtyfp': 'wt', '28yfp':'simple'}
for i, promoter in enumerate(tqdm.tqdm(promoter_dict.keys())):
    # Isolate the folders. 
    samps = glob.glob(f'{data_dir}{promoter}_snaps/*/')
    
    # Iterate through each snapshot
    for j, samp in enumerate(tqdm.tqdm(samps)):
        # Split the foldernames to get identifiers
        strain, atc, xan = samp.split('snaps/')[1].split('_')
        atc = float(atc.split('ngml')[0])
        xan = float(xan.split('mgml')[0])
        
        # Parse the clists for each position. 
        snap_samples = act.process.parse_clists(glob.glob(f'{samp}xy*/clist.mat'))
        snap_df = act.process.morphological_filter(snap_samples, ip_dist=IP_DIST)
        
        # Restrict the dataframe to relevant parameters
        snap_df = snap_df[['area_birth', 'aspect_ratio', 
                           'fluor1_mean_death', 'fluor2_mean_death', 
                           'position']].copy()
        # Rename the columns to something meaningful. 
        snap_df.rename(columns={'area_birth': 'area_pix', 
                                'fluor1_mean_death': 'mean_yfp',
                                'fluor2_mean_death': 'mean_mch',
                                }, inplace=True)
        # Add identifiers. 
        snap_df['strain'] = strain
        snap_df['atc_ngml'] = atc
        snap_df['xan_mgml'] = xan
        snap_df['promoter'] = promoter_dict[promoter]
        
        # Add to storage list. 
        snap_dfs.append(snap_df)
        
# Concatenate the lists and save. 
snap_df = pd.concat(snap_dfs)
snap_df.to_csv(f'output/{DATE}_snapshots.csv', index=False)