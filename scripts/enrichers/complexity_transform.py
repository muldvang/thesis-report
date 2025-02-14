#!/usr/bin/python3

'''Transform a data file by adding more relevant columns.'''

import pandas as pd
import sys
import os

if not len(sys.argv) == 2:
    print("Please provide filename")
    exit(1)

path = str(sys.argv[1])

df = pd.io.parsers.read_table(path, sep=' ')
df.columns = ["frequency", "simple_pre_time", "simple_running_time",
              "simple_total_time", "zipHMMlib_pre_time", "zipHMMlib_running_time",
              "zipHMMlib_total_time", "zipHMMlib_path_pre_time",
              "zipHMMlib_path_running_time", "zipHMMlib_path_total_time"]

# Add more columns.
df['zipHMMlib_total_ratio'] = df['simple_total_time'] / df['zipHMMlib_total_time']
df['zipHMMlib_path_total_ratio'] = df['simple_total_time'] / df['zipHMMlib_path_total_time']
df['zipHMMlib_running_ratio'] = df['simple_running_time'] / df['zipHMMlib_running_time']
df['zipHMMlib_path_running_ratio'] = df['simple_running_time'] / df['zipHMMlib_path_running_time']

file_name, file_extension = os.path.splitext(path)

df.to_csv(file_name + "_transformed" + file_extension, sep='\t', index=False)
