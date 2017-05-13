#!/usr/bin/python3

my_lines = []
flag = True
while(flag):
    try:
        line = input()
        line.rstrip()
        my_lines.append(line)
    except EOFError:
        flag = False

print ("Let us print list of lines")

for l in my_lines:
    print (l)
