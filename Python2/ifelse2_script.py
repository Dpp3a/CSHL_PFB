#!/usr/bin/env python3

import sys
my_number = int(sys.argv[1])

if my_number > 0:
  if my_number < 50:
      if my_number%2==0:
        print('Number is positive, even and smaller than 50')
      else:
        print('Number is positive, uneven and smaller than 50')
  else:
    if my_number%3==0:
      print('Number is positive, larger than 50 and divisible by 3')
    else:
      print('Number is positive and larger than 50')
elif my_number == 0:
  print('Number is 0')
else:
  print('Number is negative')

