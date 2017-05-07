# Numpy 

* ndarray - generic multidimensional container for homegeneous data 
* shape - tuple indicating size of each dimension 
* dtype - an object indicating data type of the array 


```
>>> import numpy as np 
>>> data = ([0.1000, 0.1200, 0.1300, 0.1400], [0.2100, 0.2200, 0.2300, 0.2400])
>>> n_data = np.array(data)
>>> n_data.shape
(2, 4)
>>> n_data.dtype  
dtype('float64')
>>> 

```
## Additional Functions to create special ndarray

### zeros

```
>>> o = np.zeros(5)
>>> print(o)
[ 0.  0.  0.  0.  0.]
>>> o.dtype
dtype('float64')
>>> o.size
5

```

### Ones

```
>>> one = np.ones(7)
>>> print(one)
[ 1.  1.  1.  1.  1.  1.  1.]
>>> one.dtype
dtype('float64')
>>> one.shape
(7,)
>>> one.size
7
>>> 

```

### empty 

```

>>> e = np.empty(9)
>>> print(e)
[  6.90268625e-310   6.90268625e-310   2.03650144e-316   6.90264011e-310
   2.37151510e-322   2.37151510e-322   2.03589354e-316   6.90268625e-310
   2.03650381e-316]
>>> e.dtype
dtype('float64')
>>> 

```
## Practice - one

* Read File 100_meter.csv using Python
* Declare “finish_time”, “year” Lists  - empty lists
* Remove white-spaces with the help of regex
* Read Line by Line, Split Each lines at “,” 
* Append first element in year list & second element in finish_time list. 
* Create 2-Dimentional numpy array 

```

import re
year = []
finish_time = []
with open("100m_running.csv", "r") as file:
    for line in file:
        line = re.sub("\s+", "", line)
        line_elements = line.split(",")
        if line_elements[0] != '':
             year.append(int(line_elements[0]))
        if line_elements[1] != '':
            finish_time.append(float(line_elements[1]))
# Here I have two lists. year & speed_time 
athelets = np.array([year, finish_time])
print(athelets)

```


## Operation between Arrays and Scalars

```

>>> my_array = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
>>> my_array.dtype
dtype('float64')
>>> my_array * my_array
array([[  1.,   4.,   9.],
       [ 16.,  25.,  36.]])
>>> my_array - my_array
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])
>>> 1/my_array
array([[ 1.        ,  0.5       ,  0.33333333],
       [ 0.25      ,  0.2       ,  0.16666667]])
>>> my_array ** 2
array([[  1.,   4.,   9.],
       [ 16.,  25.,  36.]])
>>> 

```
## Practice  - Two 

Let us go back to 100 m running example: 

* Use np.array() to create a 2D Numpy array from "athelets". Name it "np_athelets".
* Print out the type of np_athelets.
* Print out the shape attribute of np_athelets. 

```
athelets = np.array([year, finish_time])
print (type(athelets))
print (athelets.shape)
print(athelets)
```


## Basic Indexing and Slicing 


```

>>> exp_array = np.arange(10)
>>> exp_array
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> exp_array[5]
5
>>> exp_array[0]
0
>>> exp_array[2:5]
array([2, 3, 4])
>>> exp_array[2:5]=22
>>> exp_array
array([ 0,  1, 22, 22, 22,  5,  6,  7,  8,  9])
>>> 

```
Look at other slicing stuff

```

>>> exp_array = np.arange(10)
>>> exp_array[5]
5
>>> exp_array[2:5]
array([2, 3, 4])
>>> exp_array[2:5] = 29
>>> exp_array
array([ 0,  1, 29, 29, 29,  5,  6,  7,  8,  9])
>>> my_slice = exp_array[2:5]
>>> my_slice
array([29, 29, 29])
>>> my_slice[1] = 44
>>> my_slice
array([29, 44, 29])
>>> exp_array
array([ 0,  1, 29, 44, 29,  5,  6,  7,  8,  9])
>>> my_slice[:] = 400
>>> exp_array
array([  0,   1, 400, 400, 400,   5,   6,   7,   8,   9])
>>> 

```

Look at these higher-dimentional slicing 

```
>>> import numpy as np
>>> arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> arr2d[2]
array([7, 8, 9])
>>> arr2d[0][2]
3

```

## Practice - Three 
From our Running Data

* Print out the 25th column of athelets.
* Make a new variable, np_speed, containing the entire second row of athelets.
* Select the  finish time of year 1978


# Data Vizualization 
## Introduction to Matplotlib 

### Type of Graphs 
#### Bar Chart

```
import re
import numpy as np
year = []
finish_time = []
with open("100m_running.csv", "r") as file:
    for line in file:
        line = re.sub("\s+", "", line)
        line_elements = line.split(",")
        if line_elements[0] != '':
             year.append(int(line_elements[0]))
        if line_elements[1] != '':
            finish_time.append(float(line_elements[1]))
# Here I have two lists. year & speed_time 
import matplotlib.pyplot as plt
plt.bar(year, finish_time)
plt.xlabel("Year")
plt.ylabel("Time - Finish")
plt.show()

```

You can add legends etc

```

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],[r'$-1$', r'$0$', r'$+1$'])
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left', frameon=False)

plt.show()
```


## Histogram 

```
plt.hist(finish_time, bins=5)
plt.show()
```

## Google Stock Price


```
import datetime as dt
prices = []
dates = []
with open('GOOG.txt', "r") as f:
    for line in f:
        data = line.split(",")
        prices.append(data[1])
        day_y = data[0][0:4]
        day_m = data[0][4:6]
        day_d = data[0][6:8]
        dates.append(str(day_m) + '/' + str(day_d) + '/' + str(day_y))

days = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.xlabel("Trading Days")
plt.ylabel("Stock Price")
plt.plot(days,prices)
plt.gcf().autofmt_xdate()
plt.show()
```

Bar Graphs
Box and Whiskers (Boxplots)
Frequency Distribution
Histogram 
Line Graphs
Pie Graphs
Scatter Graphs
Stemplots


* Very Important in Data Analysis
** Explore Data
** Report Insights

