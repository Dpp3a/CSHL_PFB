#!usr/bin/env Python3
import re

#In the file Python_07_nobody.txt find every occurrence of 'Nobody' and print out the position.
with open('Python_07_nobody.txt', 'r') as file_object:
    for line in file_object:
        found = re.search(r'Nobody',line)
        if found:
            print(found.start())

#In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).
with open('Python_07_nobody.txt', 'r') as file_object, open('Python_07_klaus.txt', 'w') as file_object2:
    for line in file_object:
        klaus = re.sub(r'Nobody', 'Klaus', line)
        print(klaus)
        file_object2.write(klaus)
print('End of nobody code')
        
#Using pattern matching, find all the header lines in Python_07.fasta.
with open('Python_07.fasta', 'r') as file_object:
    for line in file_object:
        match = re.search(r'^>(\S+)\s(.*)', line)
        if match:
            print('ID: {}\tDES: {}'.format(match.group(1), match.group(2)))
