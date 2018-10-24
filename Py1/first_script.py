#!/usr/bin/env python3
import sys		#sys is required to input command line parameters
name = sys.argv[1]	#first command line parameter
color = sys.argv[2]
activity = sys.argv[3]
animal = sys.argv[4]

# this prints stuff
# print('My name:',name,', My favorite color:',color,', My favoite activity:',activity,', My favorite animal:',animal)
# print('My name:'+name+', My favorite color:'+color+', My favoite activity:'+activity+', My favorite animal:'+animal)
print('My name:',name+', My favorite color:',color+', My favoite activity:',activity+', My favorite animal:',animal)

