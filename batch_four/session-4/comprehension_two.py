#!/usr/bin/python3

a_dict = {'a': 1, 'b': 2, 'c': 3}
print (a_dict)


new_dict =  {value:key for key, value in a_dict.items()}
print (new_dict)

