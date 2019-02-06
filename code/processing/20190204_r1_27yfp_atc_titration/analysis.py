# -*- coding: utf-8 -*-
import sys 
sys.path.insert(0, '../../../')
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

# Define the experimental constants. 
DATE = '20190204'
RUN_NO = 1
PROMOTER = '27yfp'
APPROX_CAL_FACTOR = 6E3 # in a.u. / molecule
# Load the data. 
data = pd.read_csv(f'output/{DATE}_snapshots.csv')

# Compute the autofluorescence in mCherry and YFP 
mean_auto_yfp = data[(data['strain']=='auto')]['mean_yfp'].mean()
mean_auto_mch = data[(data['strain']=='auto')]['mean_mch'].mean()

# Subtract the autofluorescence from each. 
data['mean_yfp_corr'] = data['mean_yfp'] - mean_auto_yfp
data['mean_mch_corr'] = data['mean_mch'] - mean_auto_mch

# Compute the mean delta YFP
mean_delta_yfp = data[data['strain']=='delta']['mean_yfp_corr'].mean()

# Compute the total mCherry 
data['total_mch'] = data['mean_mch_corr'] * data['area_pix']
data['appx_activators'] = data['total_mch'] / APPROX_CAL_FACTOR

# Compute the fold-change
data['fold_change'] = data['mean_yfp_corr'] / mean_delta_yfp

# Save it to disk. 
data.to_csv(f'output/{DATE}_foldchange.csv')


