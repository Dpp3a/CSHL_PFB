#!usr/bin/#!/usr/bin/env python3

import sys

#capture command line arguments: kmer length, fasta file and number of top kmers to report
kmer_length = int(sys.argv[1])
filename_fastq = sys.argv[2]
num_top_kmers = int(sys.argv[3])

#dictionary to store the (kmer, count) data
kmer_dict = {}

#function to count kmers
def count_kmers(kmer_dict, kmer_length, sequence):
    for i in range(0, len(sequence) - kmer_length +1):
        #extract kmer as substring:
        kmer = sequence[i:(i+kmer_length)]
        if kmer in kmer_dict:
            kmer_dict[kmer] += 1
        else:
            kmer_dict[kmer] = 1

#parse sequences from fastq file
open_fastq = open(filename_fastq, 'r')
counter = 0
#gives line that we are on in fastq file (useful to extract only the line that has the sequence information)

for line in open_fastq:
    line = line.rstrip()
    counter += 1
    if counter % 4 == 2:        #this gives the line with the sequences
        count_kmers(kmer_dict, kmer_length, line)

#sort kmers by count, descendingly
sorted_kmers = sorted(kmer_dict.keys(), key = lambda x: kmer_dict[x], reverse = True)
#lambda_function defines that the key for the sort is the value and not the dictionary

#report output
counter = 0
for kmer in sorted_kmers:
    count = kmer_dict[kmer]
    print('{}\t{}'.format(kmer, count))
    counter += 1
    if counter >= num_top_kmers:
        break

sys.exit()
