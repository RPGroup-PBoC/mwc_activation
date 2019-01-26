# -*- coding: utf-8 -*_
import sys
sys.path.insert(0, '../../../')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import act.viz 
import act.bayes
import joypy as joy
colors = act.viz.personal_style()

# Experimental constants. 
DATE = 20190124

# Load the snap and lineage data.
snaps = pd.read_csv(f'output/{DATE}_snapshots.csv')
lineages = pd.read_csv(f'output/{DATE}_lineages.csv')

# Compute the calibration factor. 
model = act.bayes.StanModel('../../stan/calibration_factor.stan')

# Define the data dictionary and sample for the calibration factor. 
lineages = lineages[(lineages['I_1_tot'] > 0) & (lineages['I_2_tot'] > 0)]
data_dict = {'N': len(lineages),
            'I1': lineages['I_1_tot'],
            'I2': lineages['I_2_tot']}
samples, samples_df = model.sample(data_dict, control=dict(adapt_delta=0.95))

# ##########################################################
# CALIBRATION FACTOR PLOTS
# ##########################################################
# Compute the trend line
I_tot_range  = np.logspace(2, 7)
hpd = act.stats.compute_hpd(samples_df['alpha'], 0.95)
min_val = hpd[0] * I_tot_range
max_val = hpd[1] * I_tot_range

# Bin the data and compute the sum and fluct. 
lineages['summed'] = lineages['I_1_tot'] + lineages['I_2_tot']
lineages['fluct'] = (lineages['I_1_tot'] - lineages['I_2_tot'])**2
bins = act.stats.bin_by_events(lineages, bin_size=50)

# Instantiate figure and set labels
fig, ax = plt.subplots(1, 2, figsize=(6, 3))
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_ylabel('$(I_1 - I_2)^2$')
ax[0].set_xlabel('$I_1 + I_2$')
ax[1].set_xlabel('calibration factor [a.u. / activator]')
ax[1].set_ylabel('probability')

# Plot everything
ax[0].plot((lineages['I_1_tot'] + lineages['I_2_tot']),
           (lineages['I_1_tot'] - lineages['I_2_tot'])**2,
           '.', ms=2, label='raw data')
ax[0].plot(bins['summed'], bins['fluct'], '.', color=colors[2],
          ms=8, label='50 events/bin')
ax[0].fill_between(I_tot_range, min_val, max_val, alpha=0.5,
                  label='cred. region', color=colors[1])

ax[1].hist(samples_df['alpha'], bins=50, alpha=0.5, density=True)

# Add legend.
ax[0].legend(loc='upper left', frameon=True, fancybox=True)
plt.tight_layout()
plt.savefig('output/dilution_summary.png')

# #########################################################
# DISTRIBUTION PLOTS
# #########################################################

# Plot the distributions. 
dilution = snaps[(snaps['strain']=='dilution')]
fig, ax = plt.subplots(2, 2, figsize=(6,4))
for g, d in dilution.groupby(['atc_ngml', 'xan_mgml', 'promoter']):
    # Define th axes
    if (g[0] == 0) & (g[2] == 'simple'):
        _ax = ax[0,0] 
        _ax.set_title('simple promoter | 0 ng/ml ATC', 
                      backgroundcolor='#f1f2f6', y=1.08)
    elif (g[0] == 10) & (g[2] == 'simple'):
         _ax  = ax[1,0]
         _ax.set_title('simple promoter | 10 ng/ml ATC', 
                       backgroundcolor='#f1f2f6', y=1.08)
    elif (g[0] == 0) & (g[2] == 'wt'):
        _ax = ax[0,1] 
        _ax.set_title('wild-type promoter | 0 ng/ml ATC', 
                      backgroundcolor='#f1f2f6', y=1.08)
    elif (g[0] == 10) & (g[2] == 'wt'):
        _ax  = ax[1,1]
        _ax.set_title('wild-type promoter | 10 ng/ml ATC', 
                      backgroundcolor='#f1f2f6', y=1.08)   
        
    # Plot the ECDF
    x, y = np.sort(d['mean_yfp']), np.arange(0, len(d), 1) / len(d)
    _ax.step(x, y, lw=1, label=f'{g[1]} mg/mL')

_leg = ax[0, 0].legend(title='[xanthosine]', fancybox=True, frameon=True)
_leg.get_title().set_fontsize(8)
for a in ax.ravel():
    a.set_ylabel('cumulative distribution')
    a.set_xlabel('YFP intensity [a.u.]')
plt.tight_layout()
plt.savefig('output/yfp_distributions.png', bbox_inches='tight')
    
    
    
    
    
    
    
    
    
    