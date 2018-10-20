#!/usr/bin/env python3
import sys
my_dna = sys.argv[1]

#count nt in sequence:
print('The number of As is', my_dna.upper().count('A'))
print('The number of Ts is', my_dna.upper().count('T'))
print('The number of Cs is', my_dna.upper().count('C'))
print('The number of Gs is', my_dna.upper().count('G'))



#AT/GC content:
print('The AT content of this DNA is', (int(my_dna.count('T')) + int(my_dna.count('A'))) / len(my_dna))

print('The GC content of this DNA is', (int(my_dna.count('G')) + int(my_dna.count('C'))) / len(my_dna))
