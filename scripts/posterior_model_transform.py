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
df.columns = ["k", "simple_time", "zipHMMlib_time"]

# Add more columns.
df['zipHMMlib_ratio'] = df['simple_time'] / df['zipHMMlib_time']
df['zipHMMlib_time/k^2'] = df['zipHMMlib_time'] / df['k'] ** 2

# Compute mean and std.
grouped = df.groupby(['k'])
df2 = pd.DataFrame()
for name, group in grouped:
    # Average the measurements.
    for m in df.columns:
        group.loc[:, m + '_std'] = group.loc[:, m].std()
        group.loc[:, m] = group.loc[:, m].mean()

    # Remove duplicates
    group = group.drop_duplicates()

    group.reset_index()
    df2 = df2.append(group)

df = df2

file_name, file_extension = os.path.splitext(path)

df.to_csv(file_name + "_transformed" + file_extension, sep='\t', index=False)
