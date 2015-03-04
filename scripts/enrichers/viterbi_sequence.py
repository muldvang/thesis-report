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
df.columns = ["N", "T", "T'",

              "simple_pre_time",
              "simple_running_time",

              "simple_path_pre_time",
              "simple_path_running_time",

              "zipHMMlib_uncompressed_pre_time",
              "zipHMMlib_uncompressed_running_time",

              "zipHMMlib_uncompressed_path_pre_time",
              "zipHMMlib_uncompressed_path_running_time",

              "zipHMMlib_pre_time",
              "zipHMMlib_running_time",

              "zipHMMlib_path_pre_time",
              "zipHMMlib_path_running_time"]

# Preprocessing
df['zipHMMlib_pre_time/T'] = df['zipHMMlib_pre_time'] / df['T']

# Running time
df['zipHMMlib_running_time/T'] = df['zipHMMlib_running_time'] / df['T']
df['zipHMMlib_path_running_time/T'] = df['zipHMMlib_path_running_time'] / df['T']
df['zipHMMlib_path_backtrack_time/T'] = (df['zipHMMlib_path_running_time'] - df['zipHMMlib_running_time']) / df['T']

# Total = running time + preprocessing time
df["simple_total_time"] = df["simple_running_time"] + df["simple_pre_time"]
df["zipHMMlib_uncompressed_total_time"] = df["zipHMMlib_uncompressed_running_time"] + df["zipHMMlib_uncompressed_pre_time"]
df["zipHMMlib_uncompressed_path_total_time"] = df["zipHMMlib_uncompressed_path_running_time"] + df["zipHMMlib_uncompressed_path_pre_time"]
df["zipHMMlib_total_time"] = df["zipHMMlib_running_time"] + df["zipHMMlib_pre_time"]
df["zipHMMlib_path_total_time"] = df["zipHMMlib_path_running_time"] + df["zipHMMlib_path_pre_time"]

# Running time compared to Simple
df['zipHMMlib_uncompressed_running_ratio'] = df['simple_running_time'] / df['zipHMMlib_uncompressed_running_time']
df['zipHMMlib_uncompressed_path_running_ratio'] = df['simple_running_time'] / df['zipHMMlib_uncompressed_path_running_time']
df['zipHMMlib_running_ratio'] = df['simple_running_time'] / df['zipHMMlib_running_time']
df['zipHMMlib_path_running_ratio'] = df['simple_running_time'] / df['zipHMMlib_path_running_time']

# Total time compared to Simple
df['zipHMMlib_uncompressed_total_ratio'] = df['simple_total_time'] / df['zipHMMlib_uncompressed_total_time']
df['zipHMMlib_uncompressed_path_total_ratio'] = df['simple_total_time'] / df['zipHMMlib_uncompressed_path_total_time']
df['zipHMMlib_total_ratio'] = df['simple_total_time'] / df['zipHMMlib_total_time']
df['zipHMMlib_path_total_ratio'] = df['simple_total_time'] / df['zipHMMlib_path_total_time']

# Compression ratio
df['compression_ratio'] = df['T'] / df["T'"]

# Compute mean and std.
res = pd.DataFrame()
for _, group in df.groupby(['T']):
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
