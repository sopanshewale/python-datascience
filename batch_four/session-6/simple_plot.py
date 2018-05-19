import re
year = []
finish_time = []

with open('100_meter.csv', 'r') as f:
    for line in f:
        line = re.sub('\s+', '', line)
        line_elements = line.split(',')
        if line_elements[0] != '' and line_elements[0] != 'Year':
            year.append(int(line_elements[0]))
        if line_elements[1] != '' and line_elements[1] != 'Time':
            finish_time.append(float(line_elements[1]))
#print (year)
#print (finish_time)

import matplotlib.pyplot as plt
plt.plot(year, finish_time, 'ro')
plt.xlabel('Year')
plt.ylabel('Time - Finish')
plt.show()
