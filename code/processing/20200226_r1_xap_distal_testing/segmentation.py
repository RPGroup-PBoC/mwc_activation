#%%
import numpy as np
import pandas as pd
import skimage.io
import skimage.filters
import matplotlib.pyplot as plt
import sys 
sys.path.insert(0, '../../')
import act.viz
import act.image
import glob
colors = act.viz.pub_style()

# %%
files = glob.glob('../../../data/images/20200226_xap_distal_testing/*/pos*/')
dfs = []
for i, f in enumerate(files):
    # Parse the identifiers. 
    strain, atc, xan = f.split('/')[-3].split('_')
    atc = float(atc.split('ngml')[0])
    xan = float(xan.split('mgml')[0])
    if strain == 'xd':
        strain='distal'

    # Load the images. 
    yfp = skimage.io.imread(glob.glob(f'{f}/*c2.tif')[0])
    mch = skimage.io.imread(glob.glob(f'{f}/*c3.tif')[0])
    seg = act.image.log_segmentation(yfp, thresh=0.0001)

    # Remove small objects
    seg = skimage.morphology.remove_small_objects(seg)

    # label 
    label = skimage.measure.label(seg)

    # Compute the fluorescence region properties. 
    yfp_props = skimage.measure.regionprops(label, yfp)
    mch_props = skimage.measure.regionprops(label, mch)
    mean_yfp = []
    mean_mch = []
    area = []
    for i, _ in enumerate(yfp_props):
        mean_yfp.append(yfp_props[i]['mean_intensity'])
        mean_mch.append(mch_props[i]['mean_intensity'])
        area.append(yfp_props[i]['area'])
    
    # Assemble the data frame. 
    df = pd.DataFrame(np.array([mean_yfp, mean_mch, area]).T,
                      columns=['mean_yfp', 'mean_mch', 'area_pix'])
    df['strain'] = strain
    df['atc_ngml'] = atc
    df['xan_mgml'] = xan
    dfs.append(df)
df = pd.concat(dfs)
df.to_csv('output/20200226_xap_distal_testing.csv', index=False)

# %%
