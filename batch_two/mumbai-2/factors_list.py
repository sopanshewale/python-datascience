#!/usr/bin/python3
# We can use "range", lists with append functionality. 


number = 10
 
expected_list = []
for n in  range(number):
   tmp = []
   for i in range(n):
       if i != 0:
            if n % i  == 0:
                tmp.append(i) 
       else:
           tmp.append(i)

   expected_list.append(tmp)

#junk = expected_list.pop()
print(expected_list[1:])
