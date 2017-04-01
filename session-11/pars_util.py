#!/usr/bin/python3
from dateutil.parser import parse

d1 = parse('2017-01-25')
print (type(d1))
print (d1)
print ("-------------\n")

d2 = parse('Jan 01, 2017 10:30 AM')
print (type(d2))
print (d2)
print ("-------------\n")

d3 = parse('01/01/2017', dayfirst=True)
print (type(d3))
print (d3)
print ("-------------\n")

