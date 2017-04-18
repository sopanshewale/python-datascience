#!/usr/bin/python3
import re
import numpy as np

year = []
finish_time = []
pattern = re.compile(r'\s+')
with open("100_meter.csv", "r") as data:
      for line in data:
           line = re.sub(pattern, '', line) 
           print (line)
           tmp_list  = line.split(',')
           year.append(tmp_list[0])
           finish_time.append(tmp_list[1])


print (year)
print (finish_time)

year_n = np.array(year)
finish_time_n = np.array(finish_time)

print (year_n)
print (finish_time_n)

 
