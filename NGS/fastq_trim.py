#! usr/bin/#!/usr/bin/env python

import sys

fastq_file = open(sys.argv[1], "r")

seqs=[]

for line in fastq_file:
    line = line.rstrip("\n")
    if len(seqs) == 3: #this means you have the 4th line in the line variable
      seqs.append(line)
      #trim off five nucleotides
      print(seqs[0],seqs[1][5:],seqs[2],seqs[3][5:],sep="\n")
      seqs=[] #clear out the list to get ready for the next read
    else: #add the line to the list since you don't have all 4 lines yet
      seqs.append(line)
print(seqs)
