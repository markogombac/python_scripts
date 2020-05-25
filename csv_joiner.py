#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 05:07:20 2020

@author: Marko
"""

import os
import glob
import pandas as pd
os.chdir("/Users/Marko/Thesis_programs/Twitter_geo_data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')