#!/usr/bin/python3
from datetime import datetime

d_stamp = datetime(2017, 3, 31)
print(d_stamp)
print (str(d_stamp))
print ("---------------------\n")

# Use of strftime  - datetime to string 
print (d_stamp.strftime('%Y/%m/%d   %h:%S'))
print (d_stamp.strftime('%Y-%m-%d'))
print (d_stamp.strftime('%Y, %d %m'))
print ("---------------------\n")


# Use of strptime - strings to datetime 
d = '2017-03-31'

print (datetime.strptime(d, '%Y-%m-%d'))
print ("---------------------\n")

datestrs = ['01/Jan/2017', '01/Feb/2017', '01/Mar/2017', '01/Apr/2017']
print ([datetime.strptime(x, '%d/%b/%Y') for x in datestrs])
print ("---------------------\n")

l = [datetime.strptime(x, '%d/%b/%Y') for x in datestrs]
for d in l:
    print(d) 
