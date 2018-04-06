#!/usr/bin/python
number = int(input())

my_list = []

for i in range(number):
    tmp = []
    if i == 0:
       tmp.append(0)
    elif i == 1:
       tmp.append(1)
    else: 
        for j in range(1,i+1):
           if i % j == 0:
               tmp.append(j)
    my_list.append(tmp)


print (my_list)

 

