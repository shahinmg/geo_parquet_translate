#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 11:04:53 2025

@author: laserglaciers
"""

import geopandas as gpd
import matplotlib.pyplot as plt

#read file
fjord_num = 127

fjords_path = './separate_fjords/seperate_fjords.shp'
fjords_df = gpd.read_file(fjords_path, engine='pyogrio', use_arrow=True)

msk = fjords_df['fjord'] == fjord_num
fjord_geom = fjords_df[msk].dissolve()
fjord_geom_area = fjord_geom.area / 1e6
fjord_geom_area = fjord_geom_area[0] 


gdf = gpd.read_file('./dataframes/fjord_127.gpkg')

area_sum = gdf.groupby(['date'])[['AreaRF_km2']].sum()

ax = area_sum.plot(title=f'Fjord {fjord_num}', ylabel=r'Iceberg Area (km$^{2}$)', 
                   xlabel='', legend=None, marker='o', ms=2)
ax.grid(linestyle = '--')
area_text = ax.text(0.01,0.99, fr'Fjord Area: {fjord_geom_area:.0f} km$^{2}$', ha='left', va='top', transform=ax.transAxes)

ax.set_ylim(0,150)

fig = plt.gcf()
# fig.savefig('/media/laserglaciers/upernavik/for_kristin/fjord_127_time_series.png',dpi=300)