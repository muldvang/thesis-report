#!/usr/bin/env python

'''
Convert fasta files to the sequence format used by zipHMMlib.
'''

import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: convert_fasta_to_seq.py filename length")
    exit(1)

FILENAME = sys.argv[1]
LENGTH = int(sys.argv[2])

with open(FILENAME) as fp:
    # Drop the first line containing the fasta header.
    fp.readline()

    SEQUENCE = str(fp.read())

    REPLACEMENTS = [('\n', ''), ('A', '0'), ('C', '1'), ('G', '2'), ('T', '3')]
    for (orig, new) in REPLACEMENTS:
        SEQUENCE = SEQUENCE.replace(orig, new)

    if LENGTH > len(SEQUENCE):
        sys.stderr.write("length specified is longer than sequence!")
        exit(2)

    print(' '.join(SEQUENCE[0:LENGTH]))
