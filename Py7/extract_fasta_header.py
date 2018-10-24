#!usr/bin/env Python3
import re


#Using pattern matching, find all the header lines in Python_07.fasta. If a line matches the format of a FASTA header, extract the sequence name and description using sub patterns
#Solution1:
with open('Python_07.fasta', 'r') as file_object:
    for line in file_object:
        match = re.search(r'^>(\S+)\s(.*)', line)
        if match:
            print('ID: {}\tDES: {}'.format(match.group(1), match.group(2)))

#Solution2:
fasta_open = open('Python_07.fasta', 'r')

for line in fasta_open:
    line = line.rstrip()
    if line.startswith('>'):
        for (seq_id, desc) in re.findall(r'>(\S+)\s(.*)', line):
            print('ID: ', seq_id, '\tDescription: ', desc)

fasta_open.close()
