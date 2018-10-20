#!usr/bin/env python

#Create a new function that computes and returns the reverse complement of a sequence: it will take a DNA sequence without spaces and no header as an argument and return the reverse complement, with no spaces and no header.

my_dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'

def rev_compl(dna):
    rev_comp_dna = dna.lower().replace('a','T').replace('t','A').replace('c','G').replace('g','C')[::-1]
    return 'The reverse complement sequence is: ' + rev_comp_dna


print(rev_compl(my_dna))
