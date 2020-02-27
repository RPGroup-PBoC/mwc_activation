#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../../../')
import act.viz
colors = act.viz.pub_style()
# %%

# Load the data 
data = pd.read_csv('output/20200226_xap_distal_testing.csv')
data['area_um'] = data['area_pix'] * 0.065**2
filt = data[(data['area_um'] > 1) & (data['area_um'] < 10)]

# Set up the figure canvas. 
fig, ax = plt.subplots(2, 1, figsize=(6, 6), dpi=150)


# Plot the mcherry distributions
for g, d in filt.groupby(['strain', 'atc_ngml']):
    x = np.sort(d['mean_mch'])
    y = np.arange(len(x)) / len(x)
    ax[0].step(x, y, label=g)
ax[0].set_title('mean mCherry')

for g, d in filt.groupby(['strain', 'atc_ngml', 'xan_mgml']):
    x = np.sort(d['mean_yfp'])
    y = np.arange(len(x)) / len(x)
    ax[1].step(x, y, label=g)
ax[1].set_title('mean YFP')
ax[0].set_xscale('log')
ax[1].set_xscale('log')
ax[0].legend()
ax[1].legend()
# %%
