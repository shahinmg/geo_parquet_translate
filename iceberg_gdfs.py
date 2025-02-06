#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:42:39 2024

@author: laserglaciers
"""

import geopandas as gpd
import os


path = '/media/laserglaciers/upernavik/sid_data/coastal_bergs_out_v2/'

gdf_files = sorted([gdf for gdf in os.listdir(path) if gdf.endswith('gpkg')])
os.chdir(path)

gdf = gpd.read_file(gdf_files[0], engine='pyogrio', use_arrow=True)
os.chdir('/media/laserglaciers/upernavik/sid_data/pys/')
gdf.to_parquet('./2020-01-01_NW1_icebergs_clipped.parquet')