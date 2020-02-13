# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../../')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import act.viz
# import joypy
import glob
colors = act.viz.personal_style()

# Define the experimental parameters. 
DATE = '20180628'

# # Load the fold-change data
# fc_data = pd.read_csv(f'output/{DATE}_r{RUN_NO}_{promoter}_fold_change.csv')

# Define the list of all flow files.
gated = glob.glob(f'../../../data/flow/csv/{DATE}/*.csv')

# # Plot the mean fold-change. 
# fig, ax = plt.subplots(1, 1)
# _fc = fc_data[fc_data['strain']=='dilution']
# _fc.sort_values(by=['xan_mgml'], inplace=True)
# ax.plot(_fc['xan_mgml'], _fc['fold_change'], '--o')
# ax.set_xlabel('xanthosine [mg/mL]')
# ax.set_ylabel('fold-change')
# plt.tight_layout()
# plt.savefig('output/foldchange.png')

dfs = []
for f in gated:
    strain, xan, _ = f.split('/')[-1].split('_')
    xan = float(xan.split('mgmL')[0])
    data = pd.read_csv(f)
    data = data[data['gate']==1].copy()
    data['xan_mgml'] = xan
    data['strain'] = strain
    dfs.append(data)
dists = pd.concat(dfs)

# For plotting log(fluorescence), negative vals are bad. Offset to fix
dists['GFP-A'] += 1 + abs(dists['GFP-A'].min())


# Write my own ridgeline plot generator
n_conc = len(dists['xan_mgml'].unique())

# first plot delta & auto strains

# Set the bins 
bins = np.logspace(np.log10(dists['GFP-A'].min()),
                   np.log10(dists['GFP-A'].max()), 200)

fig, ax = plt.subplots(n_conc+1, 1, figsize=(3, 6), sharex=True)
axes = {n:ax[i] for i, n in enumerate(np.sort(dists['xan_mgml'].unique()))}

delta_dists = dists[dists['strain'] == 'delta']
for g, d in delta_dists.groupby(['xan_mgml']):
    _ = axes[g].hist(d['GFP-A'], bins=bins, density=True)#, log=True)
    _ = axes[g].set_yticks([])
    _ = axes[g].set_ylabel(f'{g}')
    
_ = ax[-1].hist(dists[dists['strain'] == 'auto']['GFP-A'],
                  bins=bins, density=True)#, log=True)
_ = ax[-1].set_yticks([])
_ = ax[-1].set_ylabel('auto')

ax[-1].set_xlabel('fluorescence [a.u.]')
ax[-1].set_xscale('log')
# for a in ax:
#     a.set_xlim([0, 1E5])

plt.tight_layout()
fig.text(-0.05, 0.55, 'xanthosine [mg/mL]', fontsize=9, rotation='vertical',
        backgroundcolor='#f1f2f6')
plt.savefig('output/deltaABR_distributions.png', bbox_inches='tight')

# now plot wt titration

fig, ax = plt.subplots(n_conc, 1, figsize=(3, 6), sharex=True)
axes = {n:ax[i] for i, n in enumerate(np.sort(dists['xan_mgml'].unique()))}

wt_dists = dists[dists['strain'] == 'WT']
for g, d in wt_dists.groupby(['xan_mgml']):
    _ = axes[g].hist(d['GFP-A'], bins=bins, density=True)#, log=True)
    _ = axes[g].set_yticks([])
    _ = axes[g].set_ylabel(f'{g}')
    
ax[-1].set_xlabel('fluorescence [a.u.]')
ax[-1].set_xscale('log')
# for a in ax:
#     a.set_xlim([0, 1E5])

plt.tight_layout()
fig.text(-0.05, 0.55, 'xanthosine [mg/mL]', fontsize=9, rotation='vertical',
        backgroundcolor='#f1f2f6')
plt.savefig('output/wt_distributions.png', bbox_inches='tight')
