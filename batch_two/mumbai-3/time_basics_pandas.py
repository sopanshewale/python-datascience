#!/usr/bin/python3
import pandas as pd
import numpy as np

from pandas import Series, DataFrame
from datetime import datetime

dates = [
          datetime(2017, 1, 1),
          datetime(2017, 1, 2),
          datetime(2017, 1, 3),
          datetime(2017, 1, 4),
          datetime(2017, 1, 5),
        ]

ts =  Series(np.random.randn(5), index=dates)
print(type(ts))
print(ts)
print ("------------\n")

print(type(ts.index))
print(ts.index)
print ("------------\n")

print (ts.index[0])
print (type(ts.index[0]))
print (ts.index.dtype)
print ("------------\n")
