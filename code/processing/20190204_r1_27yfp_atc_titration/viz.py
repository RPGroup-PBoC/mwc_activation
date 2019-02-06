# -*- coding: utf-8 -*-
import sys 
sys.path.insert(0, '../../../')
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import act.viz
colors = act.viz.personal_style()

# Define the experimental constants. 
DATE = '20190204'

# Load the fold-change data
data = pd.read_csv(f'output/{DATE}_foldchange.csv')

# Plot one - activators as a function of ATC
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
for g, d in data[data['strain']=='dilution'].groupby(['xan_mgml']):
    # Group and compute the aggregate properties. 
    _grouped = d.groupby(['atc_ngml']).agg(('mean', 'sem')).reset_index()
    ax.errorbar(_grouped['atc_ngml'], _grouped['appx_activators']['mean'],
                _grouped['appx_activators']['sem'], lw=1, capsize=1, label=g,
                fmt='.', ms=5, linestyle=':')
ax.set_xlabel('ATC [ng/mL]')            
ax.set_ylabel('activators / cell (approx)')
ax.legend(fancybox=True, title='XAN [mg/mL]')
plt.savefig('output/atc_v_repressors.png', bbox_inches='tight')

# Look at the distributions 
atc_concs = np.sort(data['atc_ngml'].unique())
fig, ax = plt.subplots(len(atc_concs), 2, figsize=(4, 6), sharex=True)
axes = {a:i for i, a in enumerate(atc_concs)}
bins = np.linspace(0, 200, 25)
for g, d in data[data['strain']=='dilution'].groupby('atc_ngml'):
    _ax = ax[axes[g], :]
    _ax[0].hist(d[d['xan_mgml']==0]['appx_activators'], bins=bins, 
                color=colors[1], alpha=0.5, density=True)
    _ax[1].hist(d[d['xan_mgml']==4]['appx_activators'], bins=bins, 
                color=colors[1], alpha=0.5, density=True)
    _ax[0].set_yticklabels([])
    _ax[1].set_yticklabels([])
    _ax[0].set_ylabel(f'{g}')
ax[0,0].set_title('0 mg/mL XAN')
ax[0, 1].set_title('4 mg/mL XAN')
ax[-1, 0].set_xlabel('activators / cell (approx)')
ax[-1, 1].set_xlabel('activators / cell (approx)')
plt.tight_layout()
plt.savefig(f'output/{DATE}_atc_distributions')

# Compute fold-change as a function of approximate activators
fig, ax = plt.subplots(1, 2, figsize=(6, 3))
for g, d in data[data['strain']=='dilution'].groupby(['xan_mgml']):
    if g == 0:
        _ax = ax[0]
    else:
        _ax = ax[1]
    _ax.plot(d['appx_activators'], d['fold_change'], '.', ms=0.5, 
        label='single cells')
    _grouped = d.groupby(['atc_ngml']).agg(('mean', 'std')).reset_index()
    _ax.errorbar(_grouped['appx_activators']['mean'], 
                _grouped['fold_change']['mean'], 
                xerr=_grouped['appx_activators']['std'],
                yerr=_grouped['fold_change']['std'], lw=1, capsize=1,
                linestyle='none', fmt='.', ms=5, color='firebrick')

for a in ax:
    a.set_xlabel('activators / cell (approx)')
    a.set_ylabel('fold-change')
    a.vlines(5, 0, a.get_ylim()[1], lw=1, color='dodgerblue')
ax[0].set_title('0 mg/mL xanthosine', backgroundcolor='#f1f2f6')
ax[1].set_title('0 mg/mL xanthosine', backgroundcolor='#f1f2f6')
plt.tight_layout()
plt.savefig(f'output/{DATE}_titration_series.png', bbox_inches='tight')

# Look at control distributions
fig, ax = plt.subplots(1, 2, figsize=(6, 3))
bins =np.linspace(-10, 10, 15)
_ = ax[0].hist(data[data['strain']=='auto']['appx_activators'], 
               bins=bins)
_ = ax[1].hist(data[data['strain']=='delta']['appx_activators'], bins=bins)

for a in ax:
    a.set_xlabel('activators / cell (approx)')
    a.set_ylabel('number of cells')
ax[0].set_title('autofluorescence control', backgroundcolor='#f1f2f6')
ax[1].set_title('∆xapR control', backgroundcolor='#f1f2f6')
plt.savefig(f'output/{DATE}_counting_controls.png')
