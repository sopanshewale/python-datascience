
**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Python - Lists, Dictionaries, Functions, Modules, Packages](#)
	- [Handling Errors](#)
		- [Demonstration](#)
		- [How to Handle Exceptions then?](#)
			- [Error Handling:](#)
			- [Closing time operation:](#)
	- [Lists](#)
		- [Iterators](#)
			- [Demonstration](#)
		- [Comprehensions](#)
			- [Demonstration](#)
	- [Dictionaries](#)
		- [Demonstration](#)
		- [Methods on Dictionaries](#)
		- [Quiz](#)
	- [Functions](#)
		- [Defining Functions](#)
		- [Demonstration](#)
		- [Quiz](#)
	- [Modules](#)
		- [Demonstrate](#)
		- [Introduce sys module](#)
			- [Quiz](#)
			- [Demonstrate](#)
		- [Modules as Scripts](#)
	- [Packages](#)
		- [Demonstrate](#)
		- [Quiz](#)


#Python - Lists, Dictionaries, Functions, Modules, Packages
---

##Handling Errors
### Demonstration 
```
#!/usr/bin/python3

while True:
    age = int(input("Your age please: "))
    print (age)

```

Talk about 

```
  File "./age.py", line 3
    while True;
              ^
SyntaxError: invalid syntax
```
and

```
root@0c280b00967b:/datascience/sessions/three# ./age.py 
  File "./age.py", line 5
    print (age)
              ^
IndentationError: unindent does not match any outer indentation level

```
and

```
root@0c280b00967b:/datascience/sessions/three# ./age.py 
Your age please: 22
22
Your age please: df  
Traceback (most recent call last):
  File "./age.py", line 4, in <module>
    age = int(input("Your age please: "))
ValueError: invalid literal for int() with base 10: 'df'

```

More Examples of Exceptions


```

# python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> a+10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> '10'+10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
>>> 


```

### How to Handle Exceptions then? 

#### Error Handling:
Python raises exceptions at runtime. 
We can catch (or ignore) and respond to the errors in our code.

If we opt to ignore the raised exception, Python's default exception-handling kicks in and stops our code with an error message. 
So, if we don't like the default way of handling exception, we may want to catch it using "try".

#### Closing time operation: 

We can use "try/finally" to guarantee the execution of a certain operation regardless of the presence or absence of exceptions in our code.


## Lists

### Iterators

An iterator is an object that allows a program to traverse through all the elements of a collection regardless of its specific implementation.

#### Demonstration 
```
#!/usr/bin/python3

iterable = ["one", "two", "three", "four"]
iterator = iter(iterable)

print ("----I")
print (type(iterator))

print ("----II")
print (next(iterator))
print ("----III")
print (next(iterator))


it = (1, 2, 3, 4, 5, 5)
s = it.__iter__()

print ("----IV")
print (s.__next__())
print ("----V")
print (s.__next__())
print ("----VI")
print (s.__next__())


```
Look at the output 

```
# ./iterators.py 
----I
<class 'list_iterator'>
----II
one
----III
two
----IV
1
----V
2
----VI
3

```


### Comprehensions 

Let us go back to Mathematics 

```
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}

```
Thats how we defined a few terms like "Set", "Vector" in Mathematics in School days, right? 


Similar stuff exists in Python

#### Demonstration

```
#!/usr/bin/python3

s = [x**2 for x in range(10)]

print("--------I")
print (s)

v = [2**i for i in range(13)]
print("--------II")
print (s)



m = [x for x in s if x % 2 == 0]
print("--------III")
print (s)

```

Look at the output: 

```
# ./comprehension.py 
--------I
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
--------II
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
--------III
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


```

And look at another code: 

```
# more comprehension_complicated.py 
#!/usr/bin/python3
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]

print ("-----------I")
print (noprimes)

primes = [x for x in range(2, 50) if x not in noprimes]

print ("-----------II")
print (primes)

```

Look at the output:

```
# ./comprehension_complicated.py 
-----------I
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 14, 21, 28, 35, 42, 49]
-----------II
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

```

Look at another interesting problem: 
```
#!/usr/bin/python3

words = 'The quick brown fox jumps over the lazy dog'.split()
print ("------------------I")
print (words)

interesting_words = [[w.upper(), w.lower(), len(w)] for w in words]

print ("------------------II")

for elements in interesting_words:
    print (elements)



```

You will get following output:

```
# ./comprehension_interesting.py 
------------------I
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
------------------II
['THE', 'the', 3]
['QUICK', 'quick', 5]
['BROWN', 'brown', 5]
['FOX', 'fox', 3]
['JUMPS', 'jumps', 5]
['OVER', 'over', 4]
['THE', 'the', 3]
['LAZY', 'lazy', 4]
['DOG', 'dog', 3]

```

## Dictionaries

Also known as: 
* *Associate Array*
* *Map*
* *Hash Map*
* *Unordered Map*

### Demonstration 
* *dictionaries.py* 

### Methods on Dictionaries 

* d.clear()
* d.copy()
* del k[d]
* dict.fromkeys(seq[, value])   (*demonstrate* - fromkeys.py) 
* iteration/accessing elements of dictionaries 
** for key in my_dictionary: 
** for key, value in my_dictionary.items():
** for value in my_dictionary.values():
** iter(d) - works very well 
** len(d)
** d.keys()
** d.values()
** d.items()
Also - discuss adding new entry into dictionary 


### Quiz

* Create a List - "A"
* List may have repeated elements 
* Create new "B", which has same element from "A" but all elements of "B" are Unique Elements 

## Functions

Let us look at the problem of converting decimal number into binary number.   

For  example:  Convert 11 into Binary Representation.  Our Typical Steps to solve this problem is: 

```
11 = 2 * 5 + 1 
```

i.e. Express 11 into  N = 2 K + B form, where B is either 0 or 1 (Every number is even or odd. Odd numbers will have B as 1 and Even numbers will have B as 0) 

Now, in next step, express 5 inton N = 2K + B form

```
5 = 2 * 2 + 1 
```

Let us go further - expression 2 

```
2 = 2 * 1 + 0 

```
And further - 1 can be expressed as 

```
1 = 2 * 0 + 1 
```
Here -  0's binary expression is : 0 and 1's binary expression. 

Anyway, so many times the code may get repeated if we need to do some task repeatedly.  
Python helps with feature of functions to avoid such  repetitions. 

### Defining Functions 

The syntax is as below: 

```
def functionname( parameters ):
      "function_docstring"
       python statements - logic/code of function 
      return [expression]
```
### Demonstration 
* function_hello.py* 
* function_dec2binary.py* 


### Quiz 

* Addition of Strings Numbers 
* Factorial  Example 
 
## Modules 

* Modules are Python files with the .py extension. 
* These files implement a set of functions and can have python statements.
* The modules can be imported from other modules using the import command.

The modules are best way to share your work, your tools with others. Those are available at - https://docs.python.org/3/library/ & https://docs.python.org/2/library/

### Demonstrate
* test_hello_module.py & hello_module.py
* How to find-out details of modules?  *dir*, *help* functions. 


### Introduce *sys* module 
* import sys
* sys.version
* sys.version_info
  
#### Quiz
* list all arguments
* It should print help if no arguments passed to the script 


#### Demonstrate 
* *one_more_exception.py* 


### Modules as Scripts
 *new_monitor.py* 

## Packages

Packages help structure Python’s module namespace by using “dotted module names”. For example, the module name *package_a.mod_b* designates a submodule named  *mod_b* in a package named *package_a*. 

The use of dotted module names saves the developers of multi-module packages  from having to worry about each other's global variable names. 



Let us assume we have the following directory structure. Here, hello.py  & monotor.py are same modules described in *Module* section, and __init__.py is an empty file:


```

mypackage
|-- __init__.py
|-- hello_module.py
`-- monitor.py

0 directories, 3 files

```


*__init__.py* helps Python to treats this directory (*/mypackage*) as package directory.  Let us assume we are working inside directory where *mypackage* directory is located.  

```
>>> from mypackage import monitor
>>> from mypackage import hello
>>> dir(monitor)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'disk', 'subprocess']
>>> dir(hello)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'goodbye', 'helloworld']
>>> hello.helloworld()
Hello World!
>>> monitor.disk("/home")
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       41251136 3970316  35544908  11% /
>>> 


```


Packages help you organise your work, help you share that with others.    As a best practice on naming conviction: packages should  have short, all-lowercase names. Try to avoid using  underscores in the names. 

### Demonstrate 
* *mypackage* directory 

### Quiz 
* create package to create factorial
* create package to create *gcd*, *hcf* of numbers






