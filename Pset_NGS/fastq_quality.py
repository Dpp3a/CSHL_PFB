#! usr/bin/#!/usr/bin/env python

import sys
fastq_file = open(sys.argv[1], "r")

#What fraction of the nucleotides in the file have a quality score greater than 30?
from Bio import SeqIO

for seq_record in SeqIO.parse(fastq_file, 'fastq'):
    quality_scores = seq_record.letter_annotations['phred_quality']
#   print(quality_scores) #a list of quality scores for each sequence
    good_score_num = 0
    bad_score_num = 0
    for score in quality_scores:
        if score >30:
            good_score_num +=1
        else:
            bad_score_num +=1
    total_score_num = bad_score_num + good_score_num
    qual_fraction = good_score_num / total_score_num
    print('The number of nucleotides with a quality score >30 is:', good_score_num)
    print('The fraction of nucleotides with a quality score >30 is:', qual_fraction)
