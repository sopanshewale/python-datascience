creation of schema

```
sqlite> CREATE TABLE presidents (
   ...>      id int primary key NOT NULL,
   ...>      name char(100) NOT NULL,
   ...>      age int NOT NULL);
sqlite> 
sqlite> .schema
CREATE TABLE presidents (
     id int primary key NOT NULL,
     name char(100) NOT NULL,
     age int NOT NULL);
sqlite> 

```

operations on databases

```
sqlite> select * from presidents;
sqlite> INSERT into presidents (id, name, age) VALUES(1, 'DONALD T', 74);
sqlite> select * from presidents;
1|DONALD T|74
sqlite> select name from presidents;
DONALD T
sqlite> INSERT into presidents (id, name, age) VALUES(2, 'Barack O', 54);
sqlite> select * from presidents;
1|DONALD T|74
2|Barack O|54
sqlite> select * from presidents order by age;
2|Barack O|54
1|DONALD T|74
sqlite> select * from presidents where id=2;
2|Barack O|54
sqlite> 

```

operations via Python3 interpretor

```
>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> type(conn)
<class 'sqlite3.Connection'>
>>> c = conn.cursor()
>>> c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
<sqlite3.Cursor object at 0x7fbebf88ee30>
>>> c.execute('''INSERT INTO stocks VALUES ('2017-01-04', 'BUY', 'GOOG', 100.0, 34.45)''')
<sqlite3.Cursor object at 0x7fbebf88ee30>
>>> conn.commit()
>>> conn.close()
>>> type(c)
<class 'sqlite3.Cursor'>


root@c563ac580153:/datascience/sessions/mumbai-3# sqlite3 example.db 
SQLite version 3.11.0 2016-02-15 17:29:24
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real);
sqlite> select * from stocks;
2017-01-04|BUY|GOOG|100.0|34.45
sqlite> 

```

work on many records

```
>>> import sqlite3
>>> conn = sqlite3.connect('example.db')
>>> c = conn.cursor()
>>> symbol = 'GOOG'
>>> c.execute("SELECT * from stocks WHERE symbol = '%s'" % symbol)
<sqlite3.Cursor object at 0x7f2dba08a730>
>>> print(c.fetchone())
('2017-01-04', 'BUY', 'GOOG', 100.0, 34.45)
>>> t = ('GOOG',)
>>> c.execute("SELECT * from stocks WHERE symbol =?", t)
<sqlite3.Cursor object at 0x7f2dba08a730>
>>> print(c.fetchone())
('2017-01-04', 'BUY', 'GOOG', 100.0, 34.45)
>>> purchases = [('2017-01-05', 'BUY', 'GOOG', 200, 35.00), ('2017-01-05', 'BUY', 'INFY', 100, 20.0), ('2017-01-07', 'SELL', 'GOOG', 50, 37.0),]
>>> c.executemany('INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', purchases)
<sqlite3.Cursor object at 0x7f2dba08a730>
>>> for row in c.execute('SELECT * from stocks ORDER BY price'):
...      print(row)
... 
('2017-01-05', 'BUY', 'INFY', 100.0, 20.0)
('2017-01-05', 'BUY', 'INFY', 100.0, 20.0)
('2017-01-04', 'BUY', 'GOOG', 100.0, 34.45)
('2017-01-05', 'BUY', 'GOOG', 200.0, 35.0)
('2017-01-05', 'BUY', 'GOOG', 200.0, 35.0)
('2017-01-07', 'SELL', 'GOOG', 50.0, 37.0)
>>> 

```

### Practice on Series

```

Fruit,Protein,Fat,Calories,Carbs
Dried Apricots,3.39,0.51,241,62.64
Raisins,4.45,0.67,434,114.81
Guava,2.3,0.86,61,12.89
Dates,0.2,0.03,23,6.23
Avocado,4.02,29.47,322,17.15

```

Pandas and Time

```
Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import pandas as pd
>>> datestrs = ['01/01/2017', '02/01/2017']
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

```

# sumarize pandas

## Initial Setup 

```
>>> import pandas
>>> import numpy
>>> import matplotlib.pyplot

```
## Object Creation 

```
>>> s = pandas.Series([1, 3, 5, numpy.nan, 6, 8])
>>> s
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
>>> 

```
>>> dates = pandas.date_range('20170423', periods=7)
>>> dates
DatetimeIndex(['2017-04-23', '2017-04-24', '2017-04-25', '2017-04-26',
               '2017-04-27', '2017-04-28', '2017-04-29'],
              dtype='datetime64[ns]', freq='D')
>>> 

```

>>> df = pandas.DataFrame(numpy.random.randn(7, 4), index = dates, columns={'dog', 'cat', 'mouse', 'duck'})
>>> df
                 cat      duck       dog     mouse
2017-04-23 -1.381724  0.178933 -1.880095  0.604224
2017-04-24  0.148233  0.208181  1.053822  0.572317
2017-04-25 -0.887622 -0.035946 -0.825040 -0.888943
2017-04-26  0.414216  0.157248  0.362521 -0.046662
2017-04-27 -1.775645  0.963451 -0.738962 -2.055655
2017-04-28 -1.356239 -0.348149  0.395081  2.154426
2017-04-29  0.096746  0.469730  0.286362  1.369842
>>> 

```

From Dictionaries 

```




