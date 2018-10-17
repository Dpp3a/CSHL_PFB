#!/usr/bin/env python3

import sys
my_dna = sys.argv[1]

#EcoR1 sequence: GAATTC

ecor1_start = int(my_dna.find('GAATTC'))+1
ecor1_end = int(my_dna.find('GAATTC'))+7

string = 'The start of the EcoR1 site is at position {}, the end is at position {}'
print(string.format(ecor1_start, ecor1_end))
