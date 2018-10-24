#!/usr/bin/env python3


#Create a DNA sequence class that will contain a sequence, its name, and it's organism of origin. Do this by creating an __init__ function.

class DNARecord(object):
#define class attributes:
    def __init__(self, sequence, sequence_name,organism):
        self.sequence = sequence
        self.sequence_name = sequence_name
        self.organism = organism
#define method: calculate and return length of sequence:
    def get_length(self):
        length = len(self.sequence)
        return length
#Nucleotide composition method a. Add in a method that caclulates and returns the nucleotide composition.
    def get_nt(self):
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        c_count = self.sequence.count('C')
        g_count = self.sequence.count('G')
        base_count = (a_count, t_count, c_count, g_count)
        return base_count
#Add in a method that caclulates and returns the GC content.
    def get_GC(self):
        length = len(self.sequence)
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        gc_content = (g_count + c_count) / length
        return gc_content

 #Add in a method that returns the sequence record in FASTA format.
    def get_fasta(self):
        fasta_format = ">{}\n{}".format(self.sequence_name, self.sequence)
        return fasta_format




#Set the name, DNA sequence, and organism for a gene.
gene_object = DNARecord('ATGATGCAATTA', 'my_gene', 'unicorn')

#Use the object sequence attribute to retrieve and print the sequence. b. uses the object name attribute to retrieve and print the name. c. uses the object organism attribute to retrieve and print the organism.
print('Sequence:', gene_object.sequence,'\n' 'Name:', gene_object.sequence_name,'\n' 'Organism:', gene_object.organism)

#get and print the sequence length
print('The sequence length is:', gene_object.get_length())

#get and print the sequence nucleotide composition
print('The number of As in the sequence is: ', gene_object.get_nt()[0], '\nThe number of Ts in the sequence is: ', gene_object.get_nt()[1], '\nThe number of Cs in the sequence is: ', gene_object.get_nt()[2], '\nThe number of Gs in the sequence is: ', gene_object.get_nt()[3])

#get and print the sequence GC content
print('The GC content is:', gene_object.get_GC())

#Write some some lines of code, outside your class (in your main program) that gets and prints the sequence in FASTA format using your new method.

print('The sequence in FASTA format is:\n',gene_object.get_fasta())
