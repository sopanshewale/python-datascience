#!/usr/bin/python3
from datetime import datetime, timedelta

start = datetime(2017, 4, 1)
print (start)


new_s = start + timedelta (12)
print (new_s)

prev_s = start - 2 * timedelta(12)

print (prev_s)

 
