#!/usr/bin/env python3

#script that takes the start and end values from the command line. If you call your script like this count.py 3 10 it will print the numbers from 3 to 10                                                                                                      
import sys
start_num = int(sys.argv[1])
end_num = int(sys.argv[2])+1

for num in range (start_num, end_num):
    if num%2==0:
        print(num)
 