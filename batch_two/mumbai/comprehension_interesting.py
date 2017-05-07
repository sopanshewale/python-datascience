#!/usr/bin/python3

words = 'The quick brown fox jumps over the lazy dog'.split()
print(type(words))
print (words)

interesting_words = [[w.upper(), w.lower(), len(w)] for w in words]

for elements in interesting_words:
    print (elements)

