#!/usr/bin/env python

#Write a simple global nucleotide alignment program of your own for sequences of similar size

seq1 = 'agtctgtca'
seq2 = 'gatctctgc'

class dna_homology(object):

#Class containing two functions to align two sequences and reverse complement one and align again
#define class attributes
    def __init__(self, dna1, dna2):
        self.dna1 = dna1
        self.dna2 = dna2

#method to align two sequences
    def alignment(self):
        score = 0
        seq_range = range(len(self.dna1))
        for nt in seq_range:
            if self.dna1[nt] == self.dna2[nt]:
                score += 1
            else:
                score -= 1
        return 'The alignment score of the two sequences is: ' + str(score)

    def alignment_rc(self):
        score = 0
        seq_range = range(len(self.dna1))
        dna1 = self.dna1.upper()
        dna2 = self.dna2.upper()
        dna1_rc  = self.dna1.lower().replace('a','T').replace('t','A').replace('c','G').replace('g','C')[::-1]
        for nt in seq_range:
            if dna1_rc[nt] == self.dna2[nt]:
                score += 1
            else:
                score -= 1
        return 'The alignment score of the two sequences is after reverse complementation of seq1: ' + str(score)


aligned_sequences = dna_homology(seq1, seq2)
print(aligned_sequences.alignment())
print(aligned_sequences.alignment_rc())



#function to align two sequences
def alignment(dna1, dna2):
    score = 0
    seq_range = range(len(dna1))
    for nt in seq_range:
        if dna1[nt] == dna2[nt]:
            score += 1
        else:
            score -= 1
    return 'The alignment score of the two sequences is: ' + str(score)

print(alignment(seq1, seq2))


#function to reverse complement dna1 and align again
def alignment_rc(dna1, dna2):
    score = 0
    seq_range = range(len(dna1))
    dna1 = dna1.upper()
    dna2 = dna2.upper()
    dna1_rc  = dna1.lower().replace('a','T').replace('t','A').replace('c','G').replace('g','C')[::-1]
    for nt in seq_range:
        if dna1_rc[nt] == dna2[nt]:
            score += 1
        else:
            score -= 1
    return 'The alignment score of the two sequences is after reverse complementation of seq1: ' + str(score)

print(alignment_rc(seq1, seq2))
