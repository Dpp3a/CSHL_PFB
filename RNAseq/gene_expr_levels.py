#!usr/bin/env python

#Write a python program that reads in the 'bowtie2.bam' file and generates a table containing the number of reads mapped to each gene.

import sys

bam_file = int(sys.argv[1])

open_bam = open(bam_file, 'r')

expression_dict = {}
