#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:42:39 2024

@author: laserglaciers
"""

import geopandas as gpd
import os
from datetime import datetime, timedelta

path = '/media/laserglaciers/upernavik/sid_data/coastal_bergs_out_v2/'
basin_path = '/media/laserglaciers/upernavik/sid_data/merged_allie_basins.gpkg'


basin_df = gpd.read_file(basin_path, engine='pyogrio', use_arrow=True)

for layer in basin_df.layer[2:]:
    
    gdf_files = sorted([gdf for gdf in os.listdir(path) if gdf.endswith('gpkg') and gdf.split('_')[1] == layer])
    
    os.chdir(path)
    gdf_list = []
    for gdf_file in gdf_files:
        date = gpd.pd.to_datetime(gdf_file[:10])
        gdf = gpd.read_file(gdf_file, engine='pyogrio', use_arrow=True)
        gdf['date'] = date
        gdf_list.append(gdf)
        
    concat_gdf = gpd.GeoDataFrame(gpd.pd.concat(gdf_list, ignore_index=True), crs=gdf_list[0].crs)
    os.chdir('/media/laserglaciers/upernavik/sid_data/out_geoparquet/')
    concat_gdf.to_parquet(f'./{layer}_icebergs_clipped.parquet')
    print(f'saved {layer}')