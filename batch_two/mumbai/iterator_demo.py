#!/usr/bin/python3

iterable = ["one", "two", "three", "four"]
iterator = iter(iterable)   # iter is function here

print (type(iterator))

print (next(iterator))
print (next(iterator))


it = (1, 2, 3, 4, 5, 5)
s = it.__iter__()

print (s.__next__())
print (s.__next__())
print (s.__next__())
