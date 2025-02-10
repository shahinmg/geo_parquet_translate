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
msk =fjords_df['fjord'] == 87
serm = fjords_df[msk].dissolve()


bergs_df = gpd.read_file(all_bergs_path, engine='pyogrio', use_arrow=True, bbox=serm)
bergs_df = bergs_df.clip(serm)


area_sum = bergs_df.groupby(['date'])[['AreaRF_m2']].sum()