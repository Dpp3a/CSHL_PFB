#!usr/bin/env Python3

#Open alpaca gene files and add the geneIDs to a Set. One Set per file.

all_genes = set()
stem_genes = set()
pigm_genes = set()
trans_factors = set()

with open('alpaca_all_genes.tsv', 'r') as file_object:
    next(file_object)
    for line in file_object:
        line = line.rstrip()
        all_genes.add(line)

with open('alpaca_stemcellproliferation_genes.tsv', 'r') as file_object:
    next(file_object)
    for line in file_object:
        line = line.rstrip()
        stem_genes.add(line)
        
with open('alpaca_pigmentation_genes.tsv', 'r') as file_object:
    next(file_object)
    for line in file_object:
        line = line.rstrip()
        pigm_genes.add(line)

print(pigm_genes)

#Find all the genes that are not cell proliferation genes.
non_prolif_genes = all_genes - stem_genes

#Find all genes that are both stem cell proliferation genes and pigment genes.
stem_pigm_genes = stem_genes & pigm_genes
print(stem_pigm_genes)

#Open 1) the transcription factor gene list file and 2) the cell proliferation gene list file. Add each to a Set, One Set per file. Find all the genes that are transcription factors for cell proliferation
with open('alpaca_transcriptionFactors.tsv', 'r') as file_object:
    next(file_object)
    for line in file_object:
        line = line.rstrip()
        trans_factors.add(line)

stem_trans_factors = stem_genes & trans_factors
print(stem_trans_factors)

