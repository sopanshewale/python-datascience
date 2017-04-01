# Timeseries data

Timeseries data is important - 
   * finance
   * economics
   * ecology 
   * ..


Pandas provide a standard set of time series tools and data algorithms...
we can use them to analyse ... almost any type of data, including server logs too :) 

## datetime Python Library 

```
1.py 

```

look at other one 

``` 
delta.py 

```



Look at the help 


```
Help on class datetime in module datetime:

class datetime(date)
 |  datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
 |  
 |  The year, month and day arguments are required. tzinfo may be None, or an
 |  instance of a tzinfo subclass. The remaining arguments may be ints.
 |  

```


demonstrate 

```
timedelta.py

```



Look at below table 


Types in datetime module 

|date| Store Calendar Date (year, month, day)|
|time| Stores time of the day - hr, minute, seconds, microseconds|
|datetime| Stores both date & time|
|timedelta| Represents difference between two datetime values - (as days, seconds & mircoseconds)|



## Strings & Datetime 

demonstrate 
```
str_1.py 
```

## dateutil.parse module 

demonstrate 

```
pars_util.py

```
## Pandas - They know handling dates
 

```
root@6879840ae648:/datascience/sessions/eleven# python3
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import pandas as pd
>>> datestrs = ['01/01/2017', '02/01/2017']
>>> pd.to_
pd.to_datetime(   pd.to_msgpack(    pd.to_numeric(    pd.to_pickle(     pd.to_timedelta(  
>>> pd.to_datetime(datestrs)
DatetimeIndex(['2017-01-01', '2017-02-01'], dtype='datetime64[ns]', freq=None)
>>> 
>>> 
>>> idx = pd.to_datetime(datestrs + [None, ''])
>>> idx
DatetimeIndex(['2017-01-01', '2017-02-01', 'NaT', 'NaT'], dtype='datetime64[ns]', freq=None)
>>> idx[3]
NaT
>>> idx[2]
NaT
>>> 
>>> pd.isnull(idx)
array([False, False,  True,  True], dtype=bool)
>>> 


## Timeseries Basics

demonstrate

```
time_basics_pandas.py

```


TimeSeries is subclass of Series 


# Handling Missing Values

Demonstrate

```
read_pima.py

```

now see  
```
replace_nan.py

```

next 

```

error_replace_nan.py

```

next

```
remove_missing_values.py

```

check next

```
calculations_on_removed_values.py

```

Replace with mean 

```
replace_with_mean.py
```

Finally 

```
finally_calculations_with_mean.py

```

