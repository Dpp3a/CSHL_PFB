#!usr/bin/env python3


#open txt file from text, read contents, uppercase each line, print each line

#get file with: wget https://raw.githubusercontent.com/prog4biol/pfb2018/master/files/Python_06.txt

with open('Python_06.txt') as file_object:
    for line in file_object:
        line = line.rstrip()
        line = line.upper()
        print(line)

#write the contents to a new file called "Python_06_uc.txt"
file_read = open('Python_06.txt','r')
file_write = open('Python_06_uc.txt', 'w')

for line in file_read:
        line = line.rstrip()
        line = line.upper()
        file_write.write(line)
        
file_read.close()
file_write.close()
print("Wrote 'Python_06_uc.txt'")

#open and write reverse complement in fasta format
with open('Python_06.seq.txt') as file_object:
    #split fasta format in 2 variables
    for line in file_object:
        seq_name,seq = line.split()
        #reverse complement the sequences:
        seq_rv = seq.replace('A', 't').replace('T','A').replace('G', 'c').replace('C', 'G').upper()[::-1]
    #change name of description that it is reverse complement and print sequences:
        print(seq_name + '_rv', seq_rv)
print('End of reverse complement command')

#Python_06.fastq: Count the number of lines and the number of characters per line. Report total number of lines, characters and average line length
line_count_total = 0
char_count_total = 0
counter = 0

with open('Python_06.fastq','r') as file_object:
    for line in file_object:
        char_count = len(line)
        char_count_total += char_count
        line = line.rstrip()
        counter = counter +1 
    avg_line_length = char_count_total/counter
    print(counter, char_count_total, avg_line_length)

