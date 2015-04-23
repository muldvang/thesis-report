#!/usr/bin/python3

'''Transform a data file by adding more relevant columns.'''

import pandas as pd
import sys
import os

if not len(sys.argv) == 2:
    print("Please provide filename")
    exit(1)

path = str(sys.argv[1])

df = pd.io.parsers.read_table(path, sep=' ', header=None)
df.columns = ["N",
              "T",
              "subseq_length",
              "simple_running_time",
              "uncompressed_running_time",
              "many_running_time"]

# Running time compared to Simple
df['uncompressed_running_ratio'] = df['simple_running_time'] / df['uncompressed_running_time']
df['one_running_ratio'] = df['simple_running_time'] / df['one_running_time']
df['many_running_ratio'] = df['simple_running_time'] / df['many_running_time']

# Compute mean and std.
res = pd.DataFrame()
for _, group in df.groupby(['subseq_length']):
    # Average the measurements.
    group_frame = pd.DataFrame()
    for c in df.columns:
        std = group.loc[:, c].std()
        mean = group.loc[:, c].mean()
        group_frame[c] = pd.Series(mean)
        group_frame[c + '_std'] = pd.Series(std)

    res = res.append(group_frame)

file_name, file_extension = os.path.splitext(path)

res.to_csv(file_name + "_transformed" + file_extension, sep=' ', index=False)
