# Numpy 

The foundation for scientific computing and data analysis in Python.  Here are a few things one can do with numpy: 

* ndarry:  multi-dimentional array proving vectorized arithmatic operations
* Mathematical operations on entire array without having to use loops
* Tools to write, read data from disk, tools to work with memory-mapped files
* Linear Algebra, Random Number Generation, and Fourier Transform capabilities. 
* Tools to integrate code with lower level languages like C, C++

The focus for learning numpy will be: 

* Fast Vectorized Array Operations for data munging & Cleaning, subsetting, and filtering, transformation and any kind of computation. 
* Common array operations - sorting, unique, & set operations

## Revisit Lists

### Couting BMI in List way

```
#!/usr/bin/python3
# bmi_lists.py
# height in inches, weight in pounds  
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]

m_height = [x * 0.0254 for x in height]
k_weight = [x * 0.453592 for x in weight]

#print (m_height)
#print (k_weight)

# kg/m^2

msqr_height = [x * x for x in m_height]
#print (msqr_height)

bmi  = [k_weight[i]/msqr_height[i] for i in range(len(msqr_height))]
print (bmi)

```

## Numpy 

### Counting bmi Numpy way 

```
#!/usr/bin/python3
#bmi_numpy.py

import numpy as np

# height in inches, weight in pounds  
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]

np_height = np.array(height)
np_weight = np.array(weight)


np_height_meters  = np_height  * 0.0254
np_weight_kgs = np_weight *  0.453592 

#print (m_height)
#print (k_weight)

# kg/m^2
 
np_height_meters_sqr  = np_height_meters ** 2
#print (msqr_height)

bmi = np_weight_kgs / np_height_meters_sqr 

print (bmi)

```



## First Numpy Array

Data Source: https://www.olympic.org/london-2012/athletics/100m-men



### Instructions 

#### One - speed  
```
# This is 2012 Olympics Game 100 meter speed result 
m_runners = [9.63, 9.75, 9.79, 9.80, 9.88, 9.94, 9.98, 11.99]

# Import the numpy package as np

# Create a Numpy array from m_runners: np_m_runners 


# Print out type of np_m_runners
print (type(np_m_runners))

```

* Import the numpy package as np
* Use np.array() to create a Numpy array from m_runners. Name this array np_m_runners
Print out the type of np_m_runners to check that you got it right.


#### Two - count height  

```
# Import numpy
import numpy as np

height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
# Create a Numpy array from height: np_height

# Print out np_height

# Convert np_height to m: np_height_m
# You need to multiply by  0.0254

# Print np_height_m


```

* Create a Numpy array from height. Name this new array np_height.
* Print np_height.
* Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
* Print out np_height_m 

#### Three - Count bmi  

```
# height in inches
# weight in pounds
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]
# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
# multiplication by  0.0254

# Create array from weight with correct units: np_weight_kg
# multiplication by 0.453592


# Calculate the BMI: bmi
# kg/m^2

# Print out bmi

```
* Create a Numpy array from the weight list with the correct units. Multiply by 0.453592 to convert from pounds to kilograms. Store the resulting Numpy array as np_weight_kg.
* Use np_height_m and np_weight_kg to calculate the BMI of each player. Use the following equation: BMI=weight(kg)/height(m)^2
* Save the resulting numpy array as bmi.
* Print out bmi.

#### Four - lightweight  

```
# height and weight are available as a regular lists

height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array

# Print out light

# Print out BMIs of all baseball players whose BMI is below 21

```

* Create a boolean Numpy array: the element of the array should be True if the corresponding runners BMI is below 21. You can use the < operator for this. Name the array light.
* Print the array light.
* Print out a Numpy array with the BMIs of all runners whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.

#### Five - Match the following

TODO - table ... include True & False 

#### Six - Subsetting 
```
height = [76.77,  70.86,  72.83,  70.07,  75.98,  70.07,  70.01, 70.8]
weight = [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]

```

* Subset np_weight: print out the element at index 5.
* Print out a sub-array of np_height: It contains the elements at index 3 up to and including index 6 
 
### Numpy - A few observations

```

>>> import numpy as np
>>> my_numpy = np.array([11.00, 12, 'numpy', True, False])
>>> type(my_numpy)
<class 'numpy.ndarray'>
>>> my_numpy
array(['11.0', '12', 'numpy', 'True', 'False'], 
      dtype='<U32')
>>> my_list = [11.00, 12, 'numpy', True, False]
>>> type(my_list)
<class 'list'>
>>> my_list + my_list
[11.0, 12, 'numpy', True, False, 11.0, 12, 'numpy', True, False]
>>> my_numpy + my_numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: ufunc 'add' did not contain a loop with signature matching types dtype('<U32') dtype('<U32') dtype('<U32')
>>> my_numpy_n = np.array([1, 2, 3])
>>> type(my_numpy_n)
<class 'numpy.ndarray'>
>>> my_numpy_n
array([1, 2, 3])
>>> my_numpy_n + my_numpy_n
array([2, 4, 6])
>>> 


```

### Numpy - Subsetting 

```
>>> import numpy as np
>>> bmi = np.array([ 24.98460153,  23.46079266,  24.25439523,  23.67718338,  26.31235232, 23.36143414,  25.29895093,  26.90200005])
>>> type(bmi)
<class 'numpy.ndarray'>
>>> bmi[1]
23.460792659999999
>>> bmi[0]
24.984601529999999
>>> bmi[11]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index 11 is out of bounds for axis 0 with size 8
>>> bmi > 24
array([ True, False,  True, False,  True, False,  True,  True], dtype=bool)
>>> bmi > 23
array([ True,  True,  True,  True,  True,  True,  True,  True], dtype=bool)
>>> bmi > 22  
array([ True,  True,  True,  True,  True,  True,  True,  True], dtype=bool)
>>> bmi[bmi > 22]
array([ 24.98460153,  23.46079266,  24.25439523,  23.67718338,
        26.31235232,  23.36143414,  25.29895093,  26.90200005])
>>> bmi[bmi > 24]
array([ 24.98460153,  24.25439523,  26.31235232,  25.29895093,  26.90200005])
>>> bmi[bmi > 25]
array([ 26.31235232,  25.29895093,  26.90200005])
>>> bmi[bmi > 26]
array([ 26.31235232,  26.90200005])
>>> bmi[bmi > 26.9]
array([ 26.90200005])
>>> 

```

