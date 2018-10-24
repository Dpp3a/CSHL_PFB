#!usr/bin/env python3

import sys
from Bio.Seq import Seq
from Bio import SeqIO

fasta_file = sys.argv[1]

nt_count = 0
contig_count = 0
contig_lens = []
total_contigs = 0

#report number of contigs in the file
for record in SeqIO.parse(fasta_file, 'fasta'):
    contig_lens.append(len(record))
    total_contigs += 1
genome = sum(contig_lens)
half_genome = genome/2
print('Total number of contigs:', total_contigs)

#report shortest and longest contig
longest = max(contig_lens)
shortest = min(contig_lens)
print('The longest contig is:', longest)
print('The shortest contig is:', shortest)

#report N50 & L50
sorted_contig_lens = sorted(contig_lens, reverse=True)
for contig_len in sorted_contig_lens:
    contig_count += 1
    nt_count += contig_len
    if nt_count >= half_genome:
        N50 = contig_len
        L50 = contig_count
        break
print('L50 is:', L50)
print('N50 is:', N50)
