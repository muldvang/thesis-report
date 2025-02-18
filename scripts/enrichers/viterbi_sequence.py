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
              "one_T'",
              "many_T'",

              "simple_pre_time",
              "simple_running_time",
              "simple_path_pre_time",
              "simple_path_running_time",

              "uncompressed_pre_time",
              "uncompressed_running_time",
              "uncompressed_path_pre_time",
              "uncompressed_path_running_time",
              "uncompressed_path_memory_running_time",

              "one_pre_time",
              "one_running_time",
              "one_path_pre_time",
              "one_path_running_time",
              "one_path_memory_running_time",

              "many_pre_time",
              "many_running_time",
              "many_path_pre_time",
              "many_path_running_time",
              "many_path_memory_running_time"]

# Preprocessing
df['many_pre_time/T'] = df['many_pre_time'] / df['T']

# Running time
df['many_running_time/T'] = df['many_running_time'] / df['T']
df['many_path_running_time/T'] = df['many_path_running_time'] / df['T']
df['many_path_backtrack_time/T'] = (df['many_path_running_time'] - df['many_running_time']) / df['T']
df['many_path_memory_running_time/T'] = df['many_path_memory_running_time'] / df['T']
df['many_path_memory_backtrack_time/T'] = (df['many_path_memory_running_time'] - df['many_running_time']) / df['T']

df["many_running_time/T'"] = df['many_running_time'] / df["many_T'"]
df["many_path_running_time/T'"] = df['many_path_running_time'] / df["many_T'"]
df["many_path_backtrack_time/T'"] = (df['many_path_running_time'] - df['many_running_time']) / df["many_T'"]
df["many_path_memory_running_time/T'"] = df['many_path_memory_running_time'] / df["many_T'"]

# Total = running time + preprocessing time
df["simple_total_time"] = df["simple_running_time"] + df["simple_pre_time"]
df["simple_path_total_time"] = df["simple_path_running_time"] + df["simple_path_pre_time"]
df["uncompressed_total_time"] = df["uncompressed_running_time"] + df["uncompressed_pre_time"]
df["uncompressed_path_total_time"] = df["uncompressed_path_running_time"] + df["uncompressed_path_pre_time"]
df["uncompressed_path_memory_total_time"] = df["uncompressed_path_memory_running_time"] + df["uncompressed_path_pre_time"]
df["one_total_time"] = df["one_running_time"] + df["one_pre_time"]
df["one_path_total_time"] = df["one_path_running_time"] + df["one_path_pre_time"]
df["one_path_memory_total_time"] = df["one_path_memory_running_time"] + df["one_path_pre_time"]
df["many_total_time"] = 500 * df["many_running_time"] + df["many_pre_time"]
df["many_path_total_time"] = 500 * df["many_path_running_time"] + df["many_path_pre_time"]
df["many_path_memory_total_time"] = 500 * df["many_path_memory_running_time"] + df["many_path_pre_time"]

# Total / T
df["simple_total_time/T"] = df["simple_total_time"] / df["T"]
df["simple_path_total_time/T"] = df["simple_path_total_time"] / df["T"]
df["uncompressed_total_time/T"] = df["uncompressed_total_time"] / df["T"]
df["uncompressed_path_total_time/T"] = df["uncompressed_path_total_time"] / df["T"]
df["uncompressed_path_memory_total_time/T"] = df["uncompressed_path_memory_total_time"] / df["T"]
df["one_total_time/T"] = df["one_total_time"] / df["T"]
df["one_path_total_time/T"] = df["one_path_total_time"] / df["T"]
df["one_path_memory_total_time/T"] = df["one_path_memory_total_time"] / df["T"]
df["many_total_time/T"] = df["many_total_time"] / df["T"] / 500
df["many_path_total_time/T"] = df["many_path_total_time"] / df["T"] / 500
df["many_path_memory_total_time/T"] = df["many_path_memory_total_time"] / df["T"] / 500

# Pre and running fraction of total time.
df["uncompressed_path_memory_pre_fraction"] = df["uncompressed_path_pre_time"] / df["uncompressed_path_memory_total_time"]
df["uncompressed_path_memory_running_fraction"] = df["uncompressed_path_memory_running_time"] / df["uncompressed_path_memory_total_time"]
df["one_path_memory_pre_fraction"] = df["one_path_pre_time"] /  df["one_path_memory_total_time"]
df["one_path_memory_running_fraction"] = df["one_path_memory_running_time"] /  df["one_path_memory_total_time"]
df["many_path_memory_pre_fraction"] = df["many_path_pre_time"] /  df["many_path_memory_total_time"]
df["many_path_memory_running_fraction"] = 500 * df["many_path_memory_running_time"] /  df["many_path_memory_total_time"]

df["uncompressed_pre_fraction"] = df["uncompressed_pre_time"] / df["uncompressed_total_time"]
df["uncompressed_running_fraction"] = df["uncompressed_running_time"] / df["uncompressed_total_time"]
df["one_pre_fraction"] = df["one_pre_time"] /  df["one_total_time"]
df["one_running_fraction"] = df["one_running_time"] /  df["one_total_time"]
df["many_pre_fraction"] = df["many_pre_time"] /  df["many_total_time"]
df["many_running_fraction"] = 500 * df["many_running_time"] /  df["many_total_time"]

# Running time compared to Simple
df['uncompressed_running_ratio'] = df['simple_running_time'] / df['uncompressed_running_time']
df['uncompressed_path_running_ratio'] = df['simple_running_time'] / df['uncompressed_path_running_time']
df['uncompressed_path_memory_running_ratio'] = df['simple_running_time'] / df['uncompressed_path_memory_running_time']
df['one_running_ratio'] = df['simple_running_time'] / df['one_running_time']
df['one_path_running_ratio'] = df['simple_running_time'] / df['one_path_running_time']
df['one_path_memory_running_ratio'] = df['simple_running_time'] / df['one_path_memory_running_time']
df['many_running_ratio'] = df['simple_running_time'] / df['many_running_time']
df['many_path_running_ratio'] = df['simple_running_time'] / df['many_path_running_time']
df['many_path_memory_running_ratio'] = df['simple_running_time'] / df['many_path_memory_running_time']

# Total time compared to Simple
df['uncompressed_total_ratio'] = df['simple_total_time'] / df['uncompressed_total_time']
df['uncompressed_path_total_ratio'] = df['simple_path_total_time'] / df['uncompressed_path_total_time']
df['uncompressed_path_memory_total_ratio'] = df['simple_path_total_time'] / df['uncompressed_path_memory_total_time']
df['one_total_ratio'] = df['simple_total_time'] / df['one_total_time']
df['one_path_total_ratio'] = df['simple_path_total_time'] / df['one_path_total_time']
df['one_path_memory_total_ratio'] = df['simple_path_total_time'] / df['one_path_memory_total_time']
df['many_total_ratio'] = 500 * df['simple_total_time'] / df['many_total_time']
df['many_path_total_ratio'] = 500 * df['simple_path_total_time'] / df['many_path_total_time']
df['many_path_memory_total_ratio'] = 500 * df['simple_path_total_time'] / df['many_path_memory_total_time']

# Compression ratio
df['many_compression_ratio'] = df['T'] / df["many_T'"]
df['one_compression_ratio'] = df['T'] / df["one_T'"]

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

res.to_csv(file_name + "_transformed" + file_extension, sep=' ', index=False, na_rep="NaN")
