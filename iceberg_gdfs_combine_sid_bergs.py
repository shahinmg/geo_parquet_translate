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


# dates_list = [date.split('\\')[-1][:10] for date in fjord_dict['1']['2021']]

basin_df = gpd.read_file(basin_path, engine='pyogrio', use_arrow=True)

# fjord_dir_list = os.listdir(path)

# years = ['2017', '2018', '2019', '2020', '2021']

# fjord_dict = {}
# for fjord_id in fjord_dir_list:
#     fjord_dir = fr'{path}\{fjord_id}'
    
#     os.chdir(fjord_dir)
#     sub_fjord_list =[fn for fn in os.listdir(fjord_dir) if fn.endswith('gpkg')]
    
#     # make a list of lists for each year for each big fjord id
#     year_dicts = {}
#     for year in years:
#         year_list = []
        
#         for sub_fjord in sub_fjord_list:
#             if sub_fjord[:4] == year:
#                 year_list.append(fr'{fjord_dir}\{sub_fjord}')
        
#         year_dicts[year] = year_list
    
#     fjord_dict[fjord_id] = year_dicts
    

    
# # start to make greenland wide distributions bi weekly
# # first get the day and month pairs. 2017 starts at 05-16
# dates_list = [date.split('\\')[-1][:10] for date in fjord_dict['1']['2021']]

# dates_dict = {}


# for fjord_id in fjord_dict:
    
#     for year in fjord_dict[fjord_id]:
        
#         for berg_file in fjord_dict[fjord_id][year]:
            
#             for date in dates_list:
#                 dates_grouped = []
                
#                 if berg_file.split('\\')[-1][:10] == date:
#                     dates_grouped.append(berg_file)
                    
#             # print(fjord_id, date)
#             dates_dict[date] = dates_grouped

    
# concat month day files 

# for month_day in month_day_dict:
#     md_list = month_day_dict[month_day]
    
#     # add date column to each file
#     for year_sub in year_sublist:
#         for biweekly_file in year_sub:
#             date_time = gpd.pd.to_datetime(biweekly_file[:10])
#             gdf = gpd.read_file(biweekly_file, engine='pyogrio', use_arrow=True)
#             gdf['date'] = date_time
    
    

# for layer in basin_df.layer[2:]:
    
#     gdf_files = sorted([gdf for gdf in os.listdir(path) if gdf.endswith('gpkg') and gdf.split('_')[1] == layer])
    
#     os.chdir(path)
#     gdf_list = []
#     for gdf_file in gdf_files:
#         date = gpd.pd.to_datetime(gdf_file[:10])
#         gdf = gpd.read_file(gdf_file, engine='pyogrio', use_arrow=True)
#         gdf['date'] = date
#         gdf_list.append(gdf)
        
#     concat_gdf = gpd.GeoDataFrame(gpd.pd.concat(gdf_list, ignore_index=True), crs=gdf_list[0].crs)
#     os.chdir('/media/laserglaciers/upernavik/sid_data/out_geoparquet/')
#     concat_gdf.to_parquet(f'./{layer}_icebergs_clipped.parquet')
#     print(f'saved {layer}')