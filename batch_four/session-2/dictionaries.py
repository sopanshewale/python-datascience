#!/usr/bin/python3

d1 = {}

print ("----------I")
print (type(d1))

d2 = {'one': 1, 'two':2}

print ("----------II")
print (d2)
print ("----------III")
print (type(d2))

d3 = dict(one=2, three=4)
print ("----------IV")
print (d3)
print (type(d3))

d4 = dict([(1, 2), (3, 4)])
print ("----------V")
print (d4)


d5 = dict({1:2, 3:4})
print ("----------V")
print (d5)
