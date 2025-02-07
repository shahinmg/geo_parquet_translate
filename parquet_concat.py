# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:40:19 2025

@author: lab-adm
"""

import geopandas as gpd
import os
from datetime import datetime, timedelta


path = r'E:\\FjordDistribution_GrIS\\out_parquets\\'
out_path = r'E:\\FjordDistribution_GrIS\\all_bergs_file\\'


parquet_list = [file for file in os.listdir(path) if file.endswith('parquet')]

concat_list = []
os.chdir(path)
for file in parquet_list:
    
    gdf = gpd.read_file(file, engine='pyogrio', use_arrow=True)
    concat_list.append(gdf)
    

concat_gdf = gpd.GeoDataFrame(gpd.pd.concat(concat_list, ignore_index=True), crs=concat_list[0].crs)
out_file  = fr'{out_path}greenland_iceberg_dist_2017-2021.parquet'
concat_gdf.to_parquet(out_file)
    