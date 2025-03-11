#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:36:24 2025

@author: laserglaciers
"""

import geopandas as gpd
import os

all_bergs_path = '/media/laserglaciers/Sid_GDrive/FjordDistribution_GrIS/all_bergs_file/greenland_iceberg_dist_2017-2021.parquet'
sep_fjord_path = '/media/laserglaciers/Sid_GDrive/FjordDistribution_GrIS/separate_fjords/seperate_fjords.shp'

fjord_df = gpd.read_file(sep_fjord_path, engine='pyogrio', use_arrow=True)
bergs_df = gpd.read_file(all_bergs_path, engine='pyogrio', use_arrow=True)

