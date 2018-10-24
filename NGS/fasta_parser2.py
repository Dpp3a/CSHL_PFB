#! usr/bin/#!/usr/bin/env python

from Bio import SeqIO

#1)Fasta parser in dictionary
id_dict = SeqIO.to_dict(SeqIO.parse('human_cds.fasta', 'fasta'))

#frequency of each Nucleotide
total_a_count = 0
total_t_count = 0
total_c_count = 0
total_g_count = 0

for seq_record in SeqIO.parse('human_cds.fasta', 'fasta'):
    a_count = seq_record.seq.count('A')
    t_count = seq_record.seq.count('T')
    c_count = seq_record.seq.count('C')
    g_count = seq_record.seq.count('G')
    total_a_count += a_count
    total_t_count += t_count
    total_c_count += c_count
    total_g_count += g_count
total_base_count = (total_a_count, total_t_count, total_c_count, total_g_count)
print('The number of As in the sequence is: ', total_base_count[0], '\nThe number of Ts in the sequence is: ', total_base_count[1], '\nThe number of Cs in the sequence is: ', total_base_count[2], '\nThe number of Gs in the sequence is: ', total_base_count[3])

# GC percentage of each sequence
gc_content_dict = {}

for seq_record in SeqIO.parse('human_cds.fasta', 'fasta'):
    seq_id = seq_record.id
    length = len(seq_record.seq)
    g_count = seq_record.seq.count('G')
    c_count = seq_record.seq.count('C')
    gc_content = (g_count + c_count) / length
    gc_content_dict[seq_id] = gc_content
print(gc_content_dict)
