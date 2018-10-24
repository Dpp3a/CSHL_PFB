#!/usr/bin/env python3

humans = 'sapiens, erectus, neanderthalensis'
print(humans)

humans_list = humans.split(',')
print(humans_list)

print(sorted(humans_list))

print(sorted(humans_list, key=len))
