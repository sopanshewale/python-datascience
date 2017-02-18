

Enter Url that contains markdown file:
https://github.com/sopanshewale/python-datascience/tree/master/session-5
GO
Paste below generated content at the top of your markdown file:

**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Modules as Scripts](#)
	- [Demonstration](#)
- [Packages](#)
	- [Objects and Classes](#)
		- [Demonstrate - my_class.py](#)
		- [Demonstrate -  my_advance_class.py](#)
	- [Sorting Objects (Instances)](#)
		- [Demonstrate -  sort_person.py](#)
		- [Quiz](#)
- [Revisiting Iterators](#)
	- [Demonstrate - Counter.py](#)
- [String Formatings](#)
	- [Demonstration](#)
	- [Quiz](#)
- [Reference -](#)
- [Regular Expressions](#)
	- [Demonstrate - simple_match.py](#)
	- [Multiple Matches](#)
		- [Demonstrate  - find_all.py](#)
	- [A Few Rules: Commonly Used RegEx symbols](#)
	- [Matching Codes](#)
	- [Mostly used functions from re module,](#)
	- [Demostrate on sub](#)
	- [Quiz](#)
	- [References](#)
- [TODO](#)
- [Next TODO](#)

---

# Modules as Scripts

A script is executable of code, run by itself. 

A module is generally a library, imported by other pieces of code.

In Python - one can use Module as script, one can use Module script as script itself. 

There is no internal distinction, The only significant difference is that when imported as a module the filename is used as the basis for the module name whereas if you execute it as a script the module is named __main__.

The module can have - 
```
if __name__=="__main__".
```

This line of code plays important role in Module to play as Script


## Demonstration 

```
# monitor.py

import subprocess
def disk (partition="/"):
     info = subprocess.call(["df", partition]) 

```

Look at following execution of Module: 

```
# python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import monitor
>>> monitor.disk()     
Filesystem     1K-blocks     Used Available Use% Mounted on
none            61890340 14778088  43945328  26% /
>>> 

```
The above file/module "monitor.py" can not run as script.   Let us modify it a little bit,


```
#!/usr/bin/python3
# new_monitor.py


import subprocess
def disk (partition="/"):
     info = subprocess.call(["df", partition]) 

if __name__ == '__main__':
    import sys
    disk(sys.argv[1]) 

```
This can act as Module as well as script 


# Packages

## Objects and Classes

### Demonstrate - my_class.py

```
#!/usr/bin/python3
class MyClass(object):
    variable = "myvalue"

    def function(self):
        print("This is a message inside the class.")


myobj = MyClass()

print (type(myobj))
print (myobj.variable)

yourobj =  MyClass()
print (yourobj.variable)

yourobj.variable = "yourvalue"

print (yourobj.variable)
yourobj.function()

```

Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

* __init__ is the constructor for a class. The self parameter refers to the instance of the object



### Demonstrate -  my_advance_class.py

```

#!/usr/bin/python3
class MyClass:
    variable = 'myvalue'
    def __init__(self, value = None):
        if value:
           self.variable = value
 

    def function(self):
        print("This is a message inside the class.")
 
    def  __repr__ (self):
         return "I am representation"

myobj = MyClass("Hello")

print (type(myobj))
print (myobj.variable)

print (myobj) 

```


## Sorting Objects (Instances)

### Demonstrate -  sort_person.py

```
# Person.py

class Person(object):
    def __init__(self, name, age):
          self.name = name
          self.age  = age
   
    def __repr__(self): 
        return "Name: %s , Age: %d \n"  % (self.name, self.age) 



```

and 

```
#!/usr/bin/python3
#  sort_person.py

from  Person import  Person

def byAge(Person):
   return Person.age

p1  = Person("Doland Trump", 70)
p2  = Person("Barack Obama", 55)
p3  = Person("G Bush", 62)
p4  = Person("Bill Clinton", 54)
p5  = Person("Ronald Reagan", 77)



presidents  = [p1, p2, p3, p4, p5]

print (presidents)

sorted_presidents = sorted(presidents,  key=byAge)

print  (sorted_presidents)

```

### Quiz
* Create Class - "City"
* Attributes  - [1] Population [2] Country
* Sort by Population
* How about adding GDP - and sort by GDP? 


# Revisiting Iterators

Python iterator objects are required to support two methods while following the iterator protocol.

* *__iter__* returns the iterator object itself. This is used in for and in statements.
* *__next__* method returns the next value from the iterator. If there is no more items to return then it should raise <nop>StopIteration exception.

## Demonstrate - Counter.py

```
# Counter.py 

class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


c = Counter(5,10)
for i in c:
   print (i, end='   ')

print ("\n")

```
Let us look at another example: 

```
# EvenNumber.py

class EvenNumber(object):
   def __init__(self, low):
        if low % 2 != 0:
           self.current =  low + 1
        else: 
           self.current = low

   def __iter__(self):
        'Returns itself as an iterator object'
        return self

   def __next__(self):
        'Returns the next value till current is lower than high'
        self.current += 2
        return self.current - 2

 
 
e = EvenNumber(2)

print (next(e))
print (next(e))
print (next(e))


```

# String Formatings 

Python supports string formatting. 

The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".


* %s - String (or any object with a string representation, like numbers)
* %d - Integers
* %f - Floating point numbers
* %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
* %x/%X - Integers in hex representation (lowercase/uppercase)

## Demonstration 

```

>>> name = "Donalt"
>>> age = 72
>>> print ("%s is %d years old " % (name, age))
Donalt is 72 years old 
>>> 
>>> mylist = [1,2,3]
>>> print("A list: %s" % mylist)
A list: [1, 2, 3]
>>> 


```

Take a look at another example: 

```

>>> class Person(object):
...     def __init__(self, name, age):
...           self.age  = age
...           self.name = name
...     def __repr__(self):
...          return "Name: " + self.name + " Age: " + str(self.age)
... 
>>> p = Person('Donald', 80)
>>> print (p)
Name: Donald Age: 80
>>> print ("The person details are : %s" % p)
The person details are : Name: Donald Age: 80
>>> 
>>> print ("The person details are : {}".format(p))
The person details are : Name: Donald Age: 80

```

## Quiz

* Create class called "Share"
* Attributes to the "Share" are: opening price, maximum price, closing price, minimum price, date field (string at this moment)
* Print share details via *__repr__* and format it nicely

# Reference - 

* https://pyformat.info/


# Regular Expressions

Let us define some rules to form some strings:

* Write a letter "a" at least once
* Append to this the letter "b" exactly five times
* Append to this the letter "c" any even number of times
* Optionally, write the letter "d" at the end

Examples of such strings are:

```
aaaabbbbbccccd
aabbbbbcc
...
```
There are infinite many such strings which satisfy above rules. 
Regular Expressions are merely a shorthand way of expressing these sets of rules.


Regex are text matching patterns described with a formal syntax
The patterns which are executed on text as input to produce either matching subset or modified version of original text
Regular Expression is kind of programming language itself - "re" module provides this functionality in Python Programming
Your friendship with re will always add advantage to your skills if you ever need to deal with Text Processing in your project.

## Demonstrate - simple_match.py

```

#!/usr/bin/python3
import re

pattern = 'Hello'
text = 'Hello Data Science Folks, How are you?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern, match.string, s, e, text[s:e]))

```

Python supports compilation of pattern - it's more efficient to compile the pattern and use it. 
The compile() function converts an expression string into a <nop>RegexObject.

Look at another examile : simple_compiled.py

```
#!/usr/bin/python3 
import re

# Precompile the patterns
regexes = [ re.compile(p) for p in ['Hello', 'Donald'] ]
text = 'Hello DataScience folks, How are you doing today?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print (type(regex)) 
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('Matchig!')
    else:
        print('No, I am not matching')

```


## Multiple Matches 

### Demonstrate  - find_all.py
```
#!/usr/bin/python3
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print (type(match) )
    print ('Found "%s"' % match)

```


*finditer()* returns an iterator that produces Match instances instead of the strings returned by *findall()*.

Another Script: find_iter.py

```
#!/usr/bin/python3

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    print (type(match))
    s = match.start()
    e = match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e))

```

## A Few Rules: Commonly Used RegEx symbols 

| symbol | Meaning | Example Pattern | Example Matches| 
|---|---|---|---|
|*| Matches Preceding Char, Subexpression, or bracked char 0 or more times | a*b* | aaaaaa, aaabbbb, bbbb|
|+| Matches Preceding Char, Subexpression, or bracked char 1 or more times | a+b+ | aaaaab, aaabbbb, abbbb|
|[] | Matches any char within bracket |[A-Z]*| APPLE, CAPITAL, |
|()| A groupd subexpression | (a*b)* | aaabaab, abaaab|
|{m, n}| Matches the preceding character, subexpression, or bracketed chars between m and n times| a{2,3}b{2,3} | |
|[^] | Matches any single character that is not in the brackets  | [^A-Z]* | aaple | 
||| Matches any char, or subexpression, separated by | | b(a|i|e)d| bad, bid, bed|
|.| Matches any single charector| b.d| bed, bzd, b$d|
|^|Beging of line| ^a|apple, an, |
|\|An Escape Char| ||
|$|Used for end of line char| [A-Z]*[a-z]*$| ABCabc, zzzyz, Bob|

## Matching Codes 

|Code|Meaning|
|---|---|
|\d|a digit|
|\D|a non-digit|
|\s|whitespace (tab, space, newline, etc.)|
|\S|non-whitespace|
|\w|alphanumeric|
|\W|non-alphanumeric|


## Mostly used functions from re module,

* compile(pattern, flags=0) – it compiles a regular expression pattern into a regular expression object, which can be used for matching using the match and search methods.
* match(pattern, string, flags=0) – if zero or more characters from the beginning of the string match, it returns a Match object, otherwise, it returns None.
* search(pattern, string, flags=0)  – similar to match(), but it scans all the string, not only it’s beginning.
* sub(pattern, repl, string, count=0, flags=0) -  Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.  repl can be either a string or a callable; if a string, backslash escapes in it are processed.  If it is a callable, it's passed the match object and must return a replacement string to be used.

## Demostrate on *sub*

```
#!/usr/bin/python3
#remove_multiple_spaces.py
import re

line = 'The   fox jumped   over    the        log'
pattern = re.compile('\s+')

line = re.sub(pattern, ' ', line)
print (line)

```

How about following expression? 

```
re.sub('\s{2,}', ' ', line)
```

## Quiz 
   * Remove starting spaces in line
   * Remove ending spaces in line
   * How about removing all digits from line? 

## References
* https://doughellmann.com/presentations/regexes-fear/#/ 
* Book - 


# TODO 
* passing options like - case insensitive 
* Multiple Lines Matching 

# Next TODO
Working with Files, Directories
Dealing with Databases
Downloading Files from  - from internet
Working with Archive Files
Working with TXT and CSV Files

