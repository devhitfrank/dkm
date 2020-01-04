#!/usr/bin/env python3
##########################################################################################
# Author: Jared L. Ostmeyer
# Date Started: 2019-08-02
# Purpose: Normalize atchley factor embedding of amino acid residues
##########################################################################################

##########################################################################################
# Libraries
##########################################################################################

import numpy as np

##########################################################################################
# Settings
##########################################################################################

path_embedding = 'atchley_factors.csv'
path_embedding_norm = 'atchley_factors_2nd,normalized.csv'

##########################################################################################
# Load data
##########################################################################################

ns = []
fs = []
with open(path_embedding, 'r') as stream:
  for line in stream:
    rows = line.split(',')
    ns.append(rows[0])
    fs.append(np.array(rows[1:], dtype=np.float32))

##########################################################################################
# Format data
##########################################################################################

fs = np.array(fs)
fs = np.concatenate(
  [fs, fs**2],
  axis=1
)
fs = (fs-np.mean(fs, axis=0))/np.std(fs, axis=0)

##########################################################################################
# Save results
##########################################################################################

with open(path_embedding_norm, 'w') as stream:
  for n, f in zip(ns, fs):
    print(n, ','.join([ str(v) for v in f ]), sep=',', file=stream)

