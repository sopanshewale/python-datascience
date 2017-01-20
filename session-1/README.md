# Session 1. Introduction to Course 

This course help you learn Python Programming Language. This is definitely not Tutorial.  
This is a carefully designed course that will train you to develop real life applications with Python.

All the sessions will demonstrate you real world code examples. The course has lot of quizzes, exercises, and projects.
This course makes sure you are able to think Python, and design and build real world applications useful for Data Science.

By the end of course - you will have enough skills to actually build real world Data Science Applications. 
 



## What is Data? 

Interaction with the candidates 

### Structured Data and Unstructured Data 


Examples: 
* Jr KG Children Result ( any menaing to: Your child is exceptionaly good at counting) - Unstructured Data 
* Xth Class Result (Mathematics - 97 marks) - Structured Data 

Question: 


#### Structured Data 

* Multi-dimensional Arrays 
 * Tabular, Spreadsheet like Data 
 * Each column may have different type of data (strings, numbers, dates) 
* Multiple Data Tables - (interrelated by key columns) (SQL Database) 
* Time Series 

Examples: 


## What's Data Science for us? 

* Hacking Skills
* Maths and Statistics Knowledge 
* Data Exploration, Preparation 
* Data Representation and Transformation 
* Computing with Data 
* Data Modeling 
* Data Presentation 

  
##  Why Python? 

so many reasons - brainstorming with students 

### History

* Started by - Guide van Rossum
* first released in 1991 
* Python 2.0 was released in  2000  (currently we have 2.7.x)   
* Python 3.0 was released in 2008  (currently we have 3.5.x) 

Open Discussion with Students 

### Features

Discussion with Students 

##  Python 2 vs Python 3  

Decided to stick to Python 3 - latest stable version 

## Community 

Discussed - where to approach to in case we are stuck on our problems 
Stackoverflow helps a lot
Documentation  - on Python.org site


## Modules  and Tools used for Data Processing 
* NumPy 
* Pandas 
* SciPy 
* Anaconda 

Question: 

## Where Python can be avoided? 

* Languages like Java or C, C++ process/run faster than Python (They are compiled one)
* Applications with low latency requirement (Think of High Frequency Trading systems) 
* Highly concurrent, multithreaded applications - avoid using Python
* Think of Global Interpreter Lock  (GIL) - a mechanism which prevents the interpreter from executing more than one Python bytecode instructions at a time

## Goal of the Course

* Learn Python tools to work productively with data
* Interact with world to get the data - files, internet resources 
* Preparation of data
* Transformation 
* Model and Computation 
* Presentation 


## Course Infrastructure

* Installation of Python 
* docker 
* git

##  Demonstration of tools used on Data 

* Example - Find out Highest NSE Index value day from 2016. Use Pandas library

```
>>> df = pd.read_csv("nse_data.csv", index_col=0)
>>> df
                Open     High      Low    Close  Shares Traded  \
Date                                                             
01-Jan-2016  7938.45  7972.55  7909.80  7963.20       64843836   
04-Jan-2016  7924.55  7937.55  7781.10  7791.30      138864905   
05-Jan-2016  7828.40  7831.20  7763.25  7784.65      149672973   
06-Jan-2016  7788.05  7800.95  7721.20  7741.00      151715828   
07-Jan-2016  7673.35  7674.95  7556.60  7568.30      194732861   
08-Jan-2016  7611.65  7634.10  7581.05  7601.35      162348690   

.
.
.
.


>>> max_nse = max(df['Close'])
>>> max_nse
8952.5
>>> day = df[df['Close'] == max_nse].index.tolist()
>>> day
['08-Sep-2016']

```


## References 

### Books 

* [Head First Python](http://www.headfirstlabs.com/books/hfpython/)
* Python for Data Analysis by Wes <nop>McKinney 

### Internet Resources (Blogs, Articles) 

* [Python Site](https://www.python.org/)
* [Google Python Course](https://developers.google.com/edu/python/)
* [NUMFOCUS](http://www.numfocus.org/) 
