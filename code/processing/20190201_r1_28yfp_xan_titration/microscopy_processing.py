# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../../')
import numpy as np
import pandas as pd
import glob
import act.process

# Define the experimental parameters. 
DATE = '20190201'
RUN_NO = 1
promoter = '28yfp'
ATC_CONC = 10
IP_DIST = 0.065


# Get the folder ids
files = glob.glob(f'../../../data/images/{DATE}_r{RUN_NO}_{promoter}_xan_titration/*')

dfs = []
for f in files:
    strain, xan = f.split('/')[-1].split('_')
    xan = float(xan.split('mgml')[0])
    xy = glob.glob(f'{f}/xy*/*.mat')
    df = act.process.parse_clists(xy) 
    df = act.process.morphological_filter(df, ip_dist=IP_DIST)
    df = df[['area_death', 'fluor1_mean_death', 'fluor2_mean_death']]
    df.rename(columns={'area_death':'area_pix', 'fluor1_mean_death':'mean_yfp', 'fluor2_mean_death':'mean_mcherry'},
             inplace=True)
    # Include identifying information. 
    df['strain'] = strain
    df['xan_mgml'] = xan
    df['atc_ngml'] = ATC_CONC
    df['date'] = DATE
    df['promoter'] = promoter
    df['run_number'] = RUN_NO
    dfs.append(df)
df = pd.concat(dfs)
df.to_csv(f'output/{DATE}_r{RUN_NO}_{promoter}_microscopy.csv')
