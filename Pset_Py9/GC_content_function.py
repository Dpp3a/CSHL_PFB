#! usr/bin/env python

#Create a new function that calculates the GC content of a DNA sequence: it will take a DNA sequence without spaces and no header as an argument and return the percentage of nucleotides that are a G or C.
def gc_content(dna):
    c_count = dna.count('C')
    g_count = dna.count('G')
    dna_len = len(dna)
    gc_content = (c_count + g_count) / dna_len
    return 'The GC content is: '+'{:.2%}'.format(gc_content)

dna4='CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
print(gc_content(dna4))
