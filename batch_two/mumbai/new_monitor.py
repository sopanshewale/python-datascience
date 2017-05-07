#!/usr/bin/python3

import subprocess
def disk (partition="/"):
     info = subprocess.call(["df", partition]) 

if __name__ == '__main__':
    import sys
    disk(sys.argv[1]) 
