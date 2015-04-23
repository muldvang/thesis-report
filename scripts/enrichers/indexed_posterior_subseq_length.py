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
              "simple_pre_time",
              "simple_running_time",
              "one_pre_time",
              "one_running_time",
              "many_pre_time",
              "many_running_time"]

# Total time
df['simple_total_time'] = df['simple_pre_time'] + df['simple_running_time']
df['one_total_time'] = df['one_pre_time'] + df['one_running_time']
df['many_total_time'] = df['many_pre_time'] + 500 * df['many_running_time']

# Running time compared to Simple
df['one_total_ratio'] = df['simple_total_time'] / df['one_total_time']
df['many_total_ratio'] = 500 * df['simple_total_time'] / df['many_total_time']

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
