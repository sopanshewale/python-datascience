
# Numpy - A few Observations 

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

# Numpy - Subsetting 

```
>>> import numpy as np
>>> bmi = np.array([24.984601531008007, 23.460792655004074, 24.254395225489343, 23.67718337604452, 26.31235232154649, 23.361434137508727, 25.298950928850154, 26.902000046937946])
>>> bmi
array([ 24.98460153,  23.46079266,  24.25439523,  23.67718338,
        26.31235232,  23.36143414,  25.29895093,  26.90200005])
>>> type(bmi)
<class 'numpy.ndarray'>
>>> bmi[1]
23.460792655004074
>>> bmi[0]
24.984601531008007
>>> bmi[11]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: index 11 is out of bounds for axis 0 with size 8
>>> bmi > 24
array([ True, False,  True, False,  True, False,  True,  True], dtype=bool)
>>> bmi > 22
array([ True,  True,  True,  True,  True,  True,  True,  True], dtype=bool)
>>> bmi[bmi>22]
array([ 24.98460153,  23.46079266,  24.25439523,  23.67718338,
        26.31235232,  23.36143414,  25.29895093,  26.90200005])
>>> bmi[bmi>26.9]
array([ 26.90200005])
>>> 

```

# N-Dimentional Arrays Numpy 

```

>>> import numpy as np
>>> data = ([0.1100, 0.1200, 0.1300, 0.1400],[0.2100, 0.2200, 0.2300, 0.2400]) 
>>> type(data)
<class 'tuple'>
>>> n_data = np.array(data)
>>> type(n_data)
<class 'numpy.ndarray'>
>>> n_data
array([[ 0.11,  0.12,  0.13,  0.14],
       [ 0.21,  0.22,  0.23,  0.24]])
>>> n_data.shape
(2, 4)
>>> n_data.dtype
dtype('float64')
>>> 

```

