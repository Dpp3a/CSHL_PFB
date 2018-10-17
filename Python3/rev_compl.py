#!/usr/bin/env python3                                                                                                                  
                                                                                                                                        
import sys
my_dna = sys.argv[1]

#complement DNA string:
#my_dna.replace('A', 't').replace('T','A').replace('G', 'c').replace('C', 'G').upper()

#reverse a DNA string:
#my_dna[::-1]

#reverse_complement:
print(my_dna.replace('A', 't').replace('T','A').replace('G', 'c').replace('C', 'G').upper()[::-1])
