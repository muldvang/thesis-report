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
              "simple_time",
              "zipHMMlib_time"]

df["zipHMMlib_time/N^2"] = df["zipHMMlib_time"] / df["N"] ** 2
df["zipHMMlib_ratio"] = df["simple_time"] / df["zipHMMlib_time"]

# Compute mean and std.
res = pd.DataFrame()
for _, group in df.groupby(['N']):
    group_frame = pd.DataFrame()
    for c in df.columns:
        mean = group.loc[:, c].mean()
        std = group.loc[:, c].std()
        group_frame[c] = pd.Series(mean)
        group_frame[c + '_std'] = pd.Series(std)

    res = res.append(group_frame)

file_name, file_extension = os.path.splitext(path)

res.to_csv(file_name + "_transformed" + file_extension, sep=' ', index=False)
