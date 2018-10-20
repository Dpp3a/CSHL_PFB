#!usr/bin/env python
import re

#Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. Use a datastructure to keep count. Print out each sequence name and its compostion in this format seqName\tA_count\tT_count\tG_count\C_count

sequences = {}
seq_name = '' 
seq = ''



with open('Python_08_test.fasta', 'r') as file_object:
#create a dictionary with seq_name as key and seq as value:
    for line in file_object:
        line = line.rstrip()
        if line.startswith('>'):
            seq_name,len,path = line.rsplit() 
            seq = ''
            sequences[seq_name] = seq
        else:
            seq += line
            sequences[seq_name] = seq
    print(sequences)

#count nucleotides:
    for header in sequences:
        print(header)
        nt_dict = {'A':0, 'T':0, 'C':0, 'G':0}
        sequence = sequences[header]
        for nt in list(sequence):
            nt_dict[nt] += 1
        print(nt_dict)

