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

for layer in basin_df.layer[2:3]:
    
    gdf_files = sorted([gdf for gdf in os.listdir(path) if gdf.endswith('gpkg') and gdf.split('_')[1] == layer])
    chunks = [gdf_files[x:x+100] for x in range(0, len(gdf_files), 12)]
    os.chdir(path)
    gdf_list = []
    
    for chunk in chunks:
        for gdf_file in chunk:
            os.chdir(path)
            # date = gpd.pd.to_datetime(gdf_file[:10])
            gdf = gpd.read_file(gdf_file, engine='pyogrio', use_arrow=True)
            gdf_list.append(gdf)
            
        concat_gdf = gpd.GeoDataFrame(gpd.pd.concat(gdf_list, ignore_index=True), crs=gdf_list[0].crs)
        os.chdir('/media/laserglaciers/upernavik/sid_data/per_file_parquet/')
        date1 = gpd.pd.to_datetime(chunk[0][:10])
        date2 = gpd.pd.to_datetime(chunk[-1][:10])
        out_file  = f'./{layer}/{layer}_{date1}_{date2}_icebergs_clipped.parquet'
        concat_gdf.to_parquet(out_file)
        print(f'saved {out_file}')