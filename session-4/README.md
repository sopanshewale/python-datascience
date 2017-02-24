
# Session 4 : Python Classes, Defining List Iterators, Regular Expressions 

---


## Dictionaries

Also known as:
* *Associate Array*
* *Map*
* *Hash Map*
* *Unordered Map*

### Demonstration
* *dictionaries.py*

```
#!/usr/bin/python3

d1 = {}

print ("----------I")
print (type(d1))

d2 = {'one': 1, 'two':2}

print ("----------II")
print (d2)
print ("----------III")
print (type(d2))
d3 = dict(one=2, three=4)
print ("----------IV")
print (d3)
print (type(d3))

d4 = dict([(1, 2), (3, 4)])
print ("----------V")
print (d4)


d5 = dict({1:2, 3:4})
print ("----------V")
print (d5)

```

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
* Develop a function - to take generic list and return sorted, unique element list (we are still talking about integers) 

## Modules

* Modules are Python files with the .py extension.
* These files implement a set of functions and can have python statements.
* The modules can be imported from other modules using the import command.

The modules are best way to share your work, your tools with others. Those are available at - https://docs.python.org/3/library/ & https://docs.python.org/2/library/

### Demonstrate
* test_hello_module.py & hello_module.py

```
#!/usr/bin/python3
# 'hello_module.py'

def helloworld():
   print ("Hello World!")

def goodbye():
   print ("Good Bye Dear!")


```

and script to use above module:

```

#!/usr/bin/python3
# 'test_hello_module.py' 

from hello_module import goodbye

print ("------I")
print (goodbye)

print ("------II")
goodbye()


```

* How to find-out details of modules?  *dir*, *help* functions.

```

# python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions']
>>> help(sys)
Help on built-in module sys:

NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.5/library/sys.html

.
.
.    

```
