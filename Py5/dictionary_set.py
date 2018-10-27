#!/usr/bin/env python3

#script in which you construct a dictionary of your favorite things
fav_dict = {'book' : 'Artemis', 'song' : 'I still remember - Bloc Party', 'tree' : 'Cedar'}

#Print out your favorite book
print(fav_dict['book']) 

#Print out your favorite book but use a variable in the key.
fav_thing = 'book'
print(fav_dict[fav_thing])

#Add your favorite 'organism' to the dictionary.
fav_dict['organism'] = 'guinea pig'

fav_thing = 'organism'
print(fav_dict[fav_thing])
print('end of command')

#print out all keys of dictionary
print(fav_dict.keys())

#Take a value from the command line for fav_thing and print the value of that item from the dictionary.
fav_thing = input('enter key here: ')
print(fav_dict[fav_thing])

#Change the value of your favorite organism.
fav_dict['organism'] = 'rabbit' 

#Get the fav_thing from the command line and a new value for that key. Change the value with the user inputted value.
fav_thing = input('enter new key here: ')
fav_value = input('enter value here: ')
fav_dict[fav_thing] = fav_value
print(fav_dict)

#Use a for loop to print out each key and value of the dictionary.
for thing in fav_dict:
    value = fav_dict[thing]
    print(thing, value)


#Write a script to find the intersection, difference, union, and symetrical difference between these two sets.
set_a = {3, 14, 15, 9, 26, 5, 35, 9}
set_b = {60, 22, 14, 0, 9}
#intersection:
set_a & set_b
#difference:
set_a - set_b
#union:
set_a | set_b
