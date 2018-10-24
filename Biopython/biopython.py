#! usr/bin/#!/usr/bin/env python

#Fasta parser using Biopython

from Bio import SeqIO

total_seq_number = 0
total_nt_number = 0

for seq_record in SeqIO.parse("seq.nt.fa", "fasta"):
  print('ID',seq_record.id)
  print('Sequence',str(seq_record.seq))
  print('Length',len(seq_record))
  print(type(seq_record)
  for line in seq_record.id:
      total_seq_number += 1
  total_nt_number += len(seq_record)

avg_seq_length = total_nt_number / total_seq_number

print('total number of sequences', total_seq_number)
print('total nt number', total_nt_number)
print('average sequence length', avg_seq_length)
