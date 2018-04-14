#!/usr/bin/python3

import sys

print (sys.argv)

# Iterate via Loop

for i in range(len(sys.argv)):
    if i == 0:
        print ("script name: ",  sys.argv[0])
    else:
        print (i, " : argument: ", sys.argv[i])
