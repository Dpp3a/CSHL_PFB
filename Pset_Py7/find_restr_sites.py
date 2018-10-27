#!usr/bin/env Python3
import re

#The enzyme ApoI has a restriction site: R^AATTY where R and Y are degenerate nucleotideides.
#R: A or G, Y: C or T
#Write a regular expression to find and print all occurrences of the site in the following sequence Python_07_ApoI.fasta.

fasta_open = open('Python_07_ApoI.fasta', 'r')


for line in fasta_open:
    line = line.rstrip()
    if not line.startswith('>'):
        for restr_site in re.findall(r'[AG]AATT[CT]',line):
            print(restr_site)

fasta_open.close()

#Determine the site(s) of the physical cut(s) by ApoI in the above sequence. Print out the sequence with "^" at the cut site.
fasta_open = open('Python_07_ApoI.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    print(line)

fasta_open = open('Python_07_ApoI.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if not line.startswith('>'):
        cut_line = line
        for site in re.finditer(r'([AG])(AATT[CT])',line):
            cut_line = re.sub(site.group(0), '^'.join([site.group(1),site.group(2)]), cut_line)
        print(cut_line)

fasta_open.close()

#Now that you've done your restriction digest, determine the lengths of your fragments and sort them by length (in the same order they would separate on an electrophoresis gel).

fasta_open = open('Python_07_ApoI.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if not line.startswith('>'):
        cut_line = line
        for site in re.finditer(r'([AG])(AATT[CT])',line):
            cut_line = re.sub(site.group(0), '^'.join([site.group(1),site.group(2)]), cut_line)
            if cut_line.find('^'):
                fragments = []
                fragments = cut_line.split('^')
            fragments = sorted(fragments, key = len)
            print(fragments)

fasta_open.close()
