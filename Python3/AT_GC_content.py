#!/usr/bin/env python3                                                                                                                          
import sys
my_dna = sys.argv[1]

print('The AT content of this DNA is', (int(my_dna.count('T')) + int(my_dna.count('A'))) / len(my_dna))

print('The GC content of this DNA is', (int(my_dna.count('G')) + int(my_dna.count('C'))) / len(my_dna))

#print the substring from nucleotide number 100 (not the same as its index) to nucleotide number 200 and count G content irrespective of case: dna5[99:199].upper().count('G')
