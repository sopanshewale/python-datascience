#Python Basics 

---


## Hello Programming 

* Talk about Docker - verify everyone is able to run Python Interpreter
* IPython 
* Jupyter
*  File vs Interactive vs Web 
* Hello Python

### Demonstration

```
#!/usr/bin/python3
print ("Hello \"World")
print ('Hello World')
print ("Hello, 'My Dear Friend'")
print ('Hello, "My Dear Friend"')
print ("One", "Two")

```
### Demonstration 
```
#!/usr/bin/python3

print("""
One
two
three
""")
print ("One", "Two")
print ("I am first line\nI am second line")

```

### Quiz

* Q1.  Which of the following statement is true about Docker? 
** 1 "docker ps" shows all containers by default
** 2 "docker ps" shows all running containers by default"

* Q. 2.  What happens when you run following command? 

```
$ docker run -d  -p 8888:8888 --name jupyter -v /Users/sopanshewale/datascience:/datascience -it sopanshewale/jupyter /bin/bash
```
** 1. A prompt from shell of the container will be thrown to you
** 2. A container is run and exited immediately
** 3. A container is run in detached mode
** 4. Docker CLI issues an error 

* Q. How to get help on IPython? 

## Comments 


### Demonstrate Script
   * *comments.py*

```
#!/usr/bin/python3

#this is a comment in Python

print ("Hello World") #This is also a comment in Python

""" This is an example of a multiline
comment that spans multiple lines
...
"""

print ("Let me try triple quotes")
'''
I am also comment
in muliple lines

'''

```

## Mathematics

Python is perfectly suited to do Mathematics. 
   * addition *+*
   * subtraction *-*
   * multiplication ***
   * division  */*

There is also support for more advanced operations such as:

   * Exponentiation ****
   * Modulo:  *%* 


### Demonstrate Script
   * *mathematics.py*

```
#!/usr/bin/python3
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

```

### Quiz

Suppose you have Rs 1000, which you can invest with a 10% return each year. 
After one year, it's 1000×1.1=1100
After two years it's 1000×1.1×1.1= 1210

How much money you end up with after 5 years? 
How much money you end up earning after 10 years? 


## Variables & Types 

Variables are nothing but reserved memory locations to store values. 

### Demonstrate Script 
   * *variables.py*

```
#!/usr/bin/python3

counter = 1000              # An integer assignment
miles   = 1050.0            # A floating point
name    = "Hari Sadu"       # A string

print ('--------------------I')
print (counter)
print (miles)
print (name)

a = b = c = 1

print ('--------------------II')
print (a)
print (b)
print (c)

print ('--------------------III')
a, b, c = 1, 2, "john"

print (a)
print (b)
print (c)

#BMI - Body Mass Index = weight/(height)^2

weight = 61.0
height = 1.79
bmi = weight / height ** 2

print ('--------------------III')
print (bmi)

print (type(bmi))


```

### Quiz
 
   * Create a variable *savings*  equal to 1000 
   * Create a variable *factor*, equal to 1.10.
   * Use *savings* and *factor* to calculate the amount of money you end up with after 8 years. 
   * Store the result in a new variable, *result*
   * Print out the value of *result*.


Python has  standard data types:

   * Numbers
      * Int
      * float 
   * String
   * Boolean - True, False 
   * List
   * Tuple
   * Dictionary


## Making Decisions

### Demonstrate Scripts 

   * if-demo.py
```
#!/usr/bin/python3
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

```

   * if-else-demo.py

```

#!/usr/bin/python3
# Program checks if the number is positive or negative
# And displays an appropriate message

num = 3

# Try these two variations as well. 
# num = -5
# num = 0

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
```


   * if-elif-else.py

```
#!/usr/bin/python3
# In this program, 
# we check if the number is positive or
# negative or zero and 
# display an appropriate message

num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")



```


## Basic Operators

   * Arithmetic Operators
   * Comparison (Relational) Operators
   * Assignment Operators
   * Logical Operators
   * Bitwise Operators
   * Membership Operators
   * Identity Operators


## Strings

   * Strings in Python are identified as a contiguous set of characters represented in the quotation marks. 
   * Python allows for either pairs of single or double quotes. 
   * Subsets of strings can be taken using the slice operator ([ ] and [:] ) 
      * with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

### Operations on Strings 
   * Concatenation - *+* 
   * Repetition - asterisk ***

### Demonostration 
   * *strings_demo.py* 

```
#!/usr/bin/python3

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

```
## Lists

Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]).

### Demonstration
   * *lists_demo.py* 

```
#!/usr/bin/python3

list     = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list )          # Prints complete list
print (list[0]  )      # Prints first element of the list
print (list[1:3] )     # Prints elements starting from 2nd till 3rd 
print (list[2:] )      # Prints elements starting from 3rd element
print (tinylist * 2 )  # Prints list two times
print (list + tinylist )# Prints concatenated lists


```

### for & while loop 

### Demonstration 
  * *while_demo.py* 

```
#!/usr/bin/python3

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1

print ("Good bye!")

```


### Operations 
We saw a few operations of lists


### Quiz
Which ones of the following lines of Python code are valid ways to build a list?

   * *A* [1, 3, 4, 2] 
   * *B* [[1, 2, 3], [4, 5, 7]] 
   * *C* [1 + 2, "a" * 5, 3]
 
## Tuples

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. *Tuples can be thought of as read-only lists* 

### Demonstration 
   * *tuples_demo.py* 

```
#!/usr/bin/python3

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)          # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists

```

## More on Lists



### Accessing Lists 
   * n = len(L)
   * item = L[index]
   * seq = L[start:stop]
   * seq = L[start:stop:step]
   * seq = L[::2] # get every other item, starting with the first
   * seq = L[1::2] # get every other item, starting with the second

### Looping Over the Lists

The for-in statement makes it easy to loop over the items in a list:

```
    for item in L:
        print (item)

```

Also look at below: 

```
for index, item in enumerate(L):
        print index, item

```
### Other important Operations
   *  L.append(item)
   *  L.extend(sequence)
   *  L.insert(index, item)
   *  del L[i]
   *  del L[i:j]
   *  item = L.pop() # last item
   *  item = L.pop(0) # first item
   *  item = L.pop(index)
   *  L.remove(item)
   * L.reverse()
   * L.sort()
   * out = sorted(L)

### Quiz 

   * Q.1.  Select the right options
```
names = ['Amir', 'Sahrukh', 'Chales', 'Dao']
print names[-1][-1]
```
So what's the output? 
   * 1. A
   * 2. r
   * 3. Amir 
   * 4. Dao 

---

   * Q. 2. What gets printed? 

```
names1 = ['Amir', 'Sahrukh', 'Chales', 'Dao']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print (sum)

```
---

   * Q. 3.  What gets printed? 

```
names1 = ['Amir', 'Sahrukh', 'Chales', 'Dao']
loc = names1.index("Edward")

print (loc) 

```
---
  
   * Q. 4. What's printed in following code? 

``` 
names1 = ['Amir', 'Sahrukh', 'Chales', 'Dao']

if 'amir' in names1:
    print (1)
else:
    print (2)

```
---

   * Q. 4. What gets printed? 
 
```
numbers = [1, 2, 3, 4]
numbers.append([5,6,7,8])

print (len(numbers))

```

---


%BLACK% *THE END* %ENDCOLOR%




