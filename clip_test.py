#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:58:38 2025

@author: m484s199
"""

import os
import geopandas as gpd

all_bergs_path = './all_bergs_file/greenland_iceberg_dist_2017-2021.parquet'

fjords_path = '/media/m484s199/Sid_GDrive/FjordDistribution_GrIS/separate_fjords/seperate_fjords.shp'

fjords_df = gpd.read_file(fjords_path, engine='pyogrio', use_arrow=True)
msk = fjords_df['fjord'] == 127
serm = fjords_df[msk].dissolve()
serm_area = serm.area / 1e6
serm_area = serm_area[0] 


bergs_df = gpd.read_file(all_bergs_path, engine='pyogrio', use_arrow=True, bbox=serm)
bergs_df = bergs_df.clip(serm)
bergs_df['AreaRF_km2'] = bergs_df['AreaRF_m2']/1e6

area_sum = bergs_df.groupby(['date'])[['AreaRF_km2']].sum()

ax = area_sum.plot(title='Sermilik Fjord', ylabel=r'Iceberg Area (km$^{2}$)', 
                   xlabel='', legend=None, marker='o', ms=2)
ax.grid(linestyle = '--')
area_text = ax.text(0.01,0.99, fr'Fjord Area: {serm_area:.0f} km$^{2}$', ha='left', va='top', transform=ax.transAxes)

ax.set_ylim(0,600)