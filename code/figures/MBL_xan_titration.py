#%%
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import joypy 
import glob
import sys
import scipy.stats
sys.path.insert(0, '../../')
import act.viz
import act.flow
colors = act.viz.pub_style()
# %%
# Parse all of hte files.
files = glob.glob('../../data/flow/csv/*.csv')
dfs = []

for f in files:
    if '2018' in f:
        date, _, strain, conc = f.split('/')[-1].split('_')
        conc = float(conc.split('mg')[0]) / 1000
        promoter = 'wt'
    elif '_XAN' in f:
        date = '20180628'
        strain, conc, _ = f.split('/')[-1].split('_')
        conc = float(conc.split('mg')[0])
        promoter = 'wt' 
    elif '27yfp' in f:
        date, _, _, strain, _, conc = f.split('/')[-1].split('_') 
        if strain == 'dilution':
            strain = 'delAB'
        elif strain == 'delta':
            strain = 'delAB_delta'
        elif strain == 'auto':
            strain = 'delAB_auto'
        conc = float(conc.split('mg')[0])
        promoter = 'wt'
    elif '28yfp' in f:
        date, _, _, strain, _, conc = f.split('/')[-1].split('_') 
        if strain == 'dilution':
            strain = 'delAB'
        elif strain == 'delta':
            strain = 'delAB_delta'
        elif strain == 'auto':
            strain = 'delAB_auto'
        conc = float(conc.split('mg')[0])
        promoter = 'proximal'

    _df = pd.read_csv(f)
    gated = act.flow.gaussian_gate(_df, 0.4)
    gated = gated[gated['gate']==1]
    keys = _df.keys()
    if 'GFP-A' in keys:
        intensity = _df['GFP-A']
    elif 'GFP' in keys:
        intensity = _df['GFP']
    elif 'FITC-H' in keys:
        intensity = _df['FITC-H']

    _df['intensity'] = np.log(intensity)
    _df['date'] = date
    _df['xan_mgml'] = conc
    _df['strain'] = strain.lower()
    _df['promoter'] = promoter
    _df = _df[['intensity', 'date', 'xan_mgml', 'strain', 'promoter']]
    dfs.append(_df) 

intensity_df = pd.concat(dfs, sort=False)

# %%
wt = intensity_df[(intensity_df['strain']=='wt') &  (intensity_df['promoter']=='wt') & (intensity_df['intensity'] > -2) & (intensity_df['intensity'] < 10)]
delta = intensity_df[(intensity_df['strain']=='delta') & (intensity_df['promoter']=='wt') & (intensity_df['intensity'] > -2) & (intensity_df['intensity'] < 10)]
delAB_wt = intensity_df[(intensity_df['date']=='20190205') & (intensity_df['strain']=='delab') &  (intensity_df['promoter']=='wt') & (intensity_df['intensity'] > 5) & (intensity_df['intensity'] < 12)] 
delAB_prox = intensity_df[(intensity_df['date']=='20190205') & (intensity_df['strain']=='delab') &  (intensity_df['promoter']=='proximal')] 
delAB_wt_delta = intensity_df[(intensity_df['strain']=='delab_delta') &  (intensity_df['promoter']=='wt') & (intensity_df['intensity'] > -5) & (intensity_df['intensity'] < 15)] 
delAB_prox_delta = intensity_df[(intensity_df['strain']=='delab_delta') &  (intensity_df['promoter']=='proximal')] 

# Rescale all of the delAB properly. 
delAB_wt_delta_mean = delAB_wt_delta['intensity'].mean()
delAB_prox_delta_mean = delAB_prox_delta['intensity'].mean()
delAB_wt['norm_int'] = delAB_wt['intensity'].values / delAB_wt_delta_mean
delAB_prox['norm_int'] = delAB_prox['intensity'].values / delAB_prox_delta_mean
# %%

_ = joypy.joyplot(delta, column='intensity', by='xan_mgml', color=colors[1],    
                figsize=(3, 4))
plt.savefig('../../figs/delta_xan_titration.pdf', bbox_inches='tight')
#%%
_ = joypy.joyplot(wt, column='intensity', by='xan_mgml', color=colors[0],
                figsize=(3, 4))
plt.savefig('../../figs/wt_xan_titration.pdf', bbox_inches='tight')
#%%
_ = joypy.joyplot(delAB_wt, column='intensity', by='xan_mgml', color=colors[2],
                figsize=(3, 4))
plt.savefig('../../figs/delAB_xan_titration.pdf', bbox_inches='tight')

# %%
# Isolate the two concentrations
wt = delAB_wt[(delAB_wt['xan_mgml']==0) | (delAB_wt['xan_mgml']==4)]
prox = delAB_prox[(delAB_prox['xan_mgml']==0) | (delAB_prox['xan_mgml']==4)]
fig, ax = plt.subplots(1, 1, figsize=(5.5, 2))
_ = joypy.joyplot(wt, by='xan_mgml', column='norm_int', color=colors[1], ax=ax)
_ = joypy.joyplot(prox, by='xan_mgml', column='norm_int', ax=ax, color=colors[0])

#%%
fig, ax = plt.subplots(1, 2, figsize=(6, 2), sharex=True)
for a in ax:
    a.tick_params(labelsize=8)
    a.tick_params(labelsize=8)
    a.yaxis.set_ticks([])


# Compute the KDEs
x_range = np.linspace(0.5, 2, 500)
wt_low_kde = scipy.stats.gaussian_kde(wt_low['norm_int'])(x_range)
wt_high_kde = scipy.stats.gaussian_kde(wt_high['norm_int'])(x_range)
prox_low_kde = scipy.stats.gaussian_kde(prox_low['norm_int'].dropna())(x_range)
prox_high_kde = scipy.stats.gaussian_kde(prox_high['norm_int'].dropna())(x_range)


ax[0].fill_between(x_range, wt_low_kde, color=colors[1], label='0 mg/mL', alpha=0.25)
ax[0].plot(x_range, wt_low_kde, '-', color=colors[1], lw=1, label='__nolegend__')
ax[0].fill_between(x_range, wt_high_kde, color=colors[0], label='4 mg/mL', alpha=0.25)
ax[0].plot(x_range, wt_high_kde, '-',color=colors[0], lw=1, label='__nolegend__')
ax[1].fill_between(x_range, prox_low_kde, color=colors[1], label='0 mg/mL', alpha=0.25)
ax[1].plot(x_range,prox_low_kde, '-', color=colors[1], lw=1, label='__nolegend__')
ax[1].fill_between(x_range, prox_high_kde, color=colors[0], label='4 mg/mL', alpha=0.25)
ax[1].plot(x_range, prox_high_kde, '--', color=colors[0], lw=1, label='__nolegend__')
ax[1].set_xlabel('fold-change in expression', fontsize=8)
ax[0].set_ylabel('density', fontsize=8)
ax[1].set_ylabel('density', fontsize=8)
for a in ax:
    leg = a.legend(title='xanthosine', fontsize=8)
    leg.get_title().set_fontsize(8)
plt.savefig('../../figs/wt_prox_comparison.svg', bbox_inches='tight')
# %%


# %%
