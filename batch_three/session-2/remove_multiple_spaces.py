#!/usr/bin/python3
import re

line = 'The   fox jumped   over    the        log'
pattern = re.compile('\s+')

print ("before")
print (line)
line = re.sub(pattern, ' ', line)
print("after")
print (line)

