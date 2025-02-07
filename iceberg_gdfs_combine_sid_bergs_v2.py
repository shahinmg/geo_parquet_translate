#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:42:39 2024

@author: laserglaciers
"""

import geopandas as gpd
import os
from datetime import datetime, timedelta

path = r'E:\FjordDistribution_GrIS\out_bergs_ms'
basin_path = r'E:\FjordDistribution_GrIS\out_bergs_ms\1\2017-05-16_icebergs_clipped.gpkg'

fjord_1_path = r'E:\\FjordDistribution_GrIS\\out_bergs_ms\\1\\'

fjord_1_list = [file for file in os.listdir(fjord_1_path) if file.endswith('gpkg')]

dates_list = [date[:10] for date in fjord_1_list]


fjord_dir_list = os.listdir(path)


# make dictonary with dates as key and values as a list of each big fjord polygon
# to make a mosiac of greenland wide iceberg distributions

dates_dicts = {}
for date in dates_list:
    sub_date_list = []
    for fjord_id in fjord_dir_list:
        fjord_dir = fr'{path}\{fjord_id}'
        sub_fjord_list =[fn for fn in os.listdir(fjord_dir) if fn.endswith('gpkg')]
        
        for sub_fjord in sub_fjord_list:
            if sub_fjord[:10] == date:
                sub_date_list.append(fr'{fjord_dir}\{sub_fjord}')
        
        dates_dicts[date] = sub_date_list
    

for date in dates_dicts:
    
    date_time_list = dates_dicts[date] # get list of file dates
    
    gdf_list = []
    for file in date_time_list:
        
        date_time = gpd.pd.to_datetime(file.split('\\')[-1][:10])
        gdf = gpd.read_file(file, engine='pyogrio', use_arrow=True)
        gdf['date'] = date_time
        date_str = str(date_time.date())
        gdf_list.append(gdf)
    
    concat_gdf = gpd.GeoDataFrame(gpd.pd.concat(gdf_list, ignore_index=True), crs=gdf_list[0].crs)
    out_file  = fr'E:\FjordDistribution_GrIS\out_parquets\{date_str}.parquet'
    concat_gdf.to_parquet(out_file)
    print(f'saved {out_file}')    
        
        
        
        
        
        
        

