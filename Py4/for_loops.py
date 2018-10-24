#!/usr/bin/env python3

#for loop to print only even values from a list of numbers
numbers = [101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
     if num%2==0:
         print(num)
print('end of loop1')

#sort list, print number, calculate sums of even and uneven numbers, print sums
numbers = [101,2,15,22,95,33,2,27,72,15,52]
sorted_numbers = sorted(numbers)
even_num = 0
uneven_num = 0
for num in sorted_numbers:
    if num%2==0:
      even_num+=num
    else:
      uneven_num+=num  
print('Sum of even numbers:', even_num, 'and sum of odds:', uneven_num)    
print('end of loop2')

#script that uses range() in a for loop to print out every number between 0 and 99
for num in range (100):
    print(num)
print('end of loop3')

#print out every number between 1 and 100
for num in range (1,101):
    print(num)
print('end of loop4')

#list comprehension to print out every number between 0 and 99
number_list = range(100)
numbers = [print(num) for num in number_list]
print('end of loop5')


#script to create a list with the following data ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']. Use a for loop to iterate through each element of this list and: Print out the length and the sequence, separated by a tab.
lengths = []
sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in sequences:
    lengths=len(seq)
    print(lengths, '\t',  seq)  
print('end of loop6')

#Modification of loop6 so that it also print out the number (postion in the list) of each sequence
lengths = []
position = []
sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in sequences:
    lengths=len(seq)
    position=sequences.index(seq)
    print(position, '\t', lengths, '\t',  seq)
print('end of loop7')



#Use list comprehension to generate a list of tuples. The tuples should contain sequences and lengths from the previous problem. Print out the length and the sequence
sequences = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
lengths = [len(seq) for seq in sequences]
print(lengths, '\t',  seq)
     

