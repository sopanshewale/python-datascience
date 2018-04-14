#!/usr/bin/python3

import subprocess
def disk (partition="/"):
     info = subprocess.call(["df", partition]) 

if __name__ == '__main__':
    import sys
    print (sys.argv[2], "Is second argument")
    disk(sys.argv[1]) 
