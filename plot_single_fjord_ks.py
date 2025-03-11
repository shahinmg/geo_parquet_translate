#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 11:04:53 2025

@author: laserglaciers
"""

import geopandas as gpd
import matplotlib.pyplot as plt

#read fjord geometry


fjords_path = './separate_fjords/Fjord1.shp'
fjords_df = gpd.read_file(fjords_path, engine='pyogrio', use_arrow=True)
fjords_df = fjords_df.to_crs(crs=3413)

fjord_geom = fjords_df.dissolve()
fjord_geom_area = fjord_geom.area / 1e6
fjord_geom_area = fjord_geom_area[0] 

# read the iceberg time series data
all_bergs_path = './all_bergs_file/greenland_iceberg_dist_2017-2021.parquet'
gdf = gpd.read_file(all_bergs_path, engine='pyogrio', use_arrow=True, bbox=fjord_geom)

bergs_df = gdf.clip(fjord_geom)
bergs_df['AreaRF_km2'] = bergs_df['AreaRF_m2']/1e6
bergs_df['X'] = bergs_df['geometry'].x
bergs_df['Y'] = bergs_df['geometry'].y


# group by date and take sum of the iceberg area
area_sum = bergs_df.groupby(['date'])[['AreaRF_km2']].sum()

ax = area_sum.plot(title=f'Fjord 1', ylabel=r'Iceberg Area (km$^{2}$)', 
                   xlabel='', legend=None, marker='o', ms=2)
ax.grid(linestyle = '--')
area_text = ax.text(0.01,0.99, fr'Fjord Area: {fjord_geom_area:.0f} km$^{2}$', ha='left', va='top', transform=ax.transAxes)

ax.set_ylim(0,40)

fig = plt.gcf()
fig.savefig('/media/laserglaciers/upernavik/for_kristin/fjord_1_time_series.png',dpi=300)

bergs_df.to_csv('./dataframes/fjord_1.csv')
bergs_df.to_file('./dataframes/fjord_1.gpkg', driver='GPKG')