#!/usr/bin/env python

import sys

#reverse_complement function
def reverse_complement(sequence):
    rev_comp = sequence.lower().replace('a','T').replace('t','A').replace('c','G').replace('g','C')[::-1]
    return rev_comp


fasta_filename = sys.argv[1]

#open fasta_file
fasta_fileobj = open(fasta_filename, 'r')

#save file to standard output: output_file = sys.stdout

#define variables
sequence_name = ''
sequence_desc = ''
sequence_string = ''

#for loop to extract gene ID and sequence
for line in fasta_fileobj:
    line = line.rstrip()
    if line.startswith('>'):
        if len(sequence_string) > 0:
            #do something with sequence, e.g. reverse complement
            rc_sequence = reverse_complement(sequence_string)
            print('>{} {}\n{}').format(sequence_name, sequence_desc, rc_sequence)
            #or to save: output_file.write('>{} {}\n{}').format(sequence_name, sequence_desc, rc_sequence)

            #re-set sequence for next looping
            sequence_string = ''

        line = line.lstrip('>')
        sequence_name, sequence_desc = line.split(maxsplit=1)
        #or: sequence_info = line.split(maxsplit=1); sequence_name = sequence_info[1]
    else:
        sequence_string += line
#at the end of the loop, there is still one sequence left that has to be processed:
if len(sequence_string>1):
    #do something with sequence, e.g. reverse complement
    rc_sequence = reverse_complement(sequence_string)
    print('>{} {}\n{}').format(sequence_name, sequence_desc, rc_sequence)
