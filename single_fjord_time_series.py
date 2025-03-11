#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 15:58:38 2025

@author: m484s199
"""

import os
import geopandas as gpd

all_bergs_path = './all_bergs_file/greenland_iceberg_dist_2017-2021.parquet'

fjords_path = './separate_fjords/seperate_fjords.shp'

fjords_df = gpd.read_file(fjords_path, engine='pyogrio', use_arrow=True)
fjord_num = 127
msk = fjords_df['fjord'] == fjord_num
fjord_geom = fjords_df[msk].dissolve()
fjord_geom_area = fjord_geom.area / 1e6
fjord_geom_area = fjord_geom_area[0] 


bergs_df = gpd.read_file(all_bergs_path, engine='pyogrio', use_arrow=True, bbox=fjord_geom)
bergs_df = bergs_df.clip(fjord_geom)
bergs_df['AreaRF_km2'] = bergs_df['AreaRF_m2']/1e6
bergs_df['X'] = bergs_df['geometry'].x
bergs_df['Y'] = bergs_df['geometry'].y

bergs_df.drop(['Count','ID'], axis=1, inplace=True)

area_sum = bergs_df.groupby(['date'])[['AreaRF_km2']].sum()

ax = area_sum.plot(title=f'Fjord {fjord_num}', ylabel=r'Iceberg Area (km$^{2}$)', 
                   xlabel='', legend=None, marker='o', ms=2)
ax.grid(linestyle = '--')
area_text = ax.text(0.01,0.99, fr'Fjord Area: {fjord_geom_area:.0f} km$^{2}$', ha='left', va='top', transform=ax.transAxes)

ax.set_ylim(0,150)