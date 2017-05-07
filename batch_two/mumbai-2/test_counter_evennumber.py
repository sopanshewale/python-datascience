#!/usr/bin/python3
from Counter import Counter
from EvenNumber import EvenNumber 

c = Counter(5,10)
for i in c:
   print (i, end='   ')

print ("\n")


e = EvenNumber(2)

print (next(e))
print (next(e))
print (next(e))
