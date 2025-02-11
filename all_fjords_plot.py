#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:38:26 2025

@author: m484s199
"""

import os
import geopandas as gpd
import matplotlib.pyplot as plt

all_bergs_path = './all_bergs_file/greenland_iceberg_dist_2017-2021.parquet'
fjords_path = '/media/m484s199/Sid_GDrive/FjordDistribution_GrIS/separate_fjords/seperate_fjords.shp'
op = './fjord_distribution_plots/'


fjords_df = gpd.read_file(fjords_path, engine='pyogrio', use_arrow=True)
good_fjords = fjords_df['fjord'].dropna()
fjords_df = fjords_df.loc[good_fjords.index]

for fjord in set(good_fjords):
    
    print(fjord)
    msk = fjords_df['fjord'] == fjord
    
    fjord_geom = fjords_df[msk].dissolve()
    fjord_geom_area = fjord_geom.area / 1e6
    fjord_geom_area = fjord_geom_area[0] 

    bergs_df = gpd.read_file(all_bergs_path, engine='pyogrio', use_arrow=True, bbox=fjord_geom)
    bergs_df = bergs_df.clip(fjord_geom)
    bergs_df['AreaRF_km2'] = bergs_df['AreaRF_m2']/1e6

    
    area_sum = bergs_df.groupby(['date'])[['AreaRF_km2']].sum()
    
    ax = area_sum.plot(title=f'Fjord {fjord:.0f}', ylabel=r'Iceberg Area (km$^{2}$)', 
                       xlabel='', legend=None, marker='o', ms=2)
    ax.grid(linestyle = '--')
    
    
    ax.grid(linestyle = '--')
    area_text = ax.text(0.01,0.99, fr'Fjord Area: {fjord_geom_area:.0f} km$^{2}$', 
                        ha='left', va='top', transform=ax.transAxes)
    # ax.set_ylim(0,1500)
    
    out_file = f'{op}fjord_{str(int(fjord))}.png'
    plt.savefig(out_file, bbox_inches='tight')
    plt.close()
    
    
    