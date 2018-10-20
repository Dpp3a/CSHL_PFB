#!/usr/bin/env python3

#Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence


sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tuples = []
for sequence in sequences:
  seq_length = len(sequence)
  tuple=(seq_length,sequence)
  tuples.append(tuple)
print(tuples)

#this is the short way to do the same thing:
tuples=[(len(sequence),sequence) for sequence in sequences]
print(tuples)

#list comprehension: [Action for Item in Seq]
