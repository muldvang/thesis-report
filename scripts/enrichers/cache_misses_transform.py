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
df.columns = ["N",
              "time",
              "L1_TCM", "L2_TCM", "L3_TCM",
              "L1_TCA", "L2_TCA", "L3_TCA", ""]

# Add more columns.
df['time/N^3'] = df['time'] / df['N'] ** 3
df['L1_pct'] = 100 * df['L1_TCM'] / df['L1_TCA']
df['L2_pct'] = 100 * df['L2_TCM'] / df['L2_TCA']
df['L3_pct'] = 100 * df['L3_TCM'] / df['L3_TCA']

file_name, file_extension = os.path.splitext(path)

df.to_csv(file_name + "_transformed" + file_extension, sep='\t', index=False)
