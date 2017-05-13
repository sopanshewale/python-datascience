#!/usr/bin/python3

def decToBin(n):
    if n==0: 
         return '0'
    else:
        return decToBin(int(n/2)) + str(n%2)

n = int(input())
l = decToBin(n)
print (l)
ones = l.split('0')
max = 0
for o in ones:
    if max < len(o):
         max = len(o)

print (max)

