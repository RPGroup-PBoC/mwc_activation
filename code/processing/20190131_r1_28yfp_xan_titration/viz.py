# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../../')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import act.viz
import joypy
import glob
colors = act.viz.personal_style()

# Define the experimental parameters. 
DATE = '20190131'
RUN_NO = 1
promoter = '28yfp'

# Load the fold-change data
fc_data = pd.read_csv(f'output/{DATE}_r{RUN_NO}_{promoter}_fold_change.csv')

# Define the list of all flow files.
gated = glob.glob(f'../../../data/flow/csv/{DATE}_r{RUN_NO}_{promoter}_dilution*.csv')

# Plot the mean fold-change. 
fig, ax = plt.subplots(1, 1)
_fc = fc_data[fc_data['strain']=='dilution']
_fc.sort_values(by=['xan_mgml'], inplace=True)
ax.plot(_fc['xan_mgml'], _fc['fold_change'], '--o')

dfs = []
for f in gated:
    _, _, _, _, _, xan = f.split('/')[-1].split('_')
    xan = float(xan.split('mgml')[0])
    data = pd.read_csv(f)
    data = data[data['gate']==1].copy()
    data['xan_mgml'] = xan
    dfs.append(data)
dists = pd.concat(dfs)

fig, ax = plt.subplots(1, 1)
for g, d in dists.groupby(['xan_mgml']):
    ax.hist(d['FITC-H'], bins= 50, label=g, alpha=0.25)
    print(g, np.var(d['FITC-H']) / np.mean(d['FITC-H']))
    
    
plt.legend()

fig, ax = plt.subplots(1, 1)
joypy.joyplot(dists, column='FITC-H', by='xan_mgml', ax=ax, colormap=plt.cm.Reds)


# Write my own ridgeline plot generator
n_conc = len(dists['xan_mgml'].unique())


# Set the bins 
bins = np.linspace(np.round(dists['FITC-H'].min()), np.round(dists['FITC-H'].max()), 100) 

fig, ax = plt.subplots(n_conc, 1, figsize=(3, 6), sharex=True, sharey=True,)
axes = {n:ax[i] for i, n in enumerate(np.sort(dists['xan_mgml'].unique()))}
axes                        
for g, d in dists.groupby(['xan_mgml']):
    _ = axes[g].hist(d['FITC-H'], bins=bins, density=True)
    _ = axes[g].set_yticks([])
    _ = axes[g].set_ylabel(f'{g}')
    
ax[-1].set_xlabel('fluorescence [a.u.]')
for a in ax:
    a.set_xlim([0, 1E5])
    
plt.tight_layout()
plt.savefig('output/ridgeline_plot.png', bbox_inches='tight')