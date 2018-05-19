# Random Walk 
* http://sphelps.net/teaching/random-walks-slides.html#/
# Pandas
* Integrated Timeseries Functionality 
# Database Operations 

# Introduction to Pandas Data Structures 
## Series 


```
>>> import pandas as pd
>>> s = pd.Series(['Usain Bolt', 9.63, 'Yohan Blake', 9.75, 'Justin Gatlin', 9.79])
>>> s
0       Usain Bolt
1             9.63
2      Yohan Blake
3             9.75
4    Justin Gatlin
5             9.79
dtype: object
>>> 

```
You can pass the index list:

```
>>> s = pd.Series(['Usain Bolt', 9.63, 'Yohan Blake', 9.75, 'Justin Gatlin', 9.79], index=['A', 'B', 'C', 'D', 'E', 'F'])
>>> s
A       Usain Bolt
B             9.63
C      Yohan Blake
D             9.75
E    Justin Gatlin
F             9.79
dtype: object
>>> 

```
You can also use dictionaries to create the series

```
>>> runners  =  {'Usain Bolt': 9.63, 'Yohan Blake': 9.75, 'Justin Gatlin': 9.79}
>>> runners
{'Yohan Blake': 9.75, 'Usain Bolt': 9.63, 'Justin Gatlin': 9.79}
>>> r = pd.Series(runners)
>>> r
Justin Gatlin    9.79
Usain Bolt       9.63
Yohan Blake      9.75
dtype: float64
>>> 

```
Accessing Elements

```

>>> r[['Yohan Blake', 'Yohan Blake']]
Yohan Blake    9.75
Yohan Blake    9.75
dtype: float64
>>> 
>>> r[['Yohan Blake', 'Usain Bolt']]
Yohan Blake    9.75
Usain Bolt     9.63
dtype: float64
>>> 

```

Look at other ways to access more elements

```
>>> runners  =  {'Usain Bolt': 9.63, 'Yohan Blake': 9.75, 'Justin Gatlin': 9.79, 'Tyson Gay': 9.8, 'Ryan Bailey': 9.88, 'Churandy Martina': 9.94, 'Richard Thompson': 9.98, 'Asafa Powell': 11.99}
>>> 
>>> r = pd.Series(runners)
>>> r
Asafa Powell        11.99
Churandy Martina     9.94
Justin Gatlin        9.79
Richard Thompson     9.98
Ryan Bailey          9.88
Tyson Gay            9.80
Usain Bolt           9.63
Yohan Blake          9.75
dtype: float64
>>> r[r>10]
Asafa Powell    11.99
dtype: float64
>>> r[r<9.8]
Justin Gatlin    9.79
Usain Bolt       9.63
Yohan Blake      9.75
dtype: float64
>>> 

```
Operations on the fly 
```

>>> r[['Superman']]
Superman   NaN
dtype: float64
>>> r['Superman']=5.0
>>> r['Batman'] = 6.0
>>> r
Asafa Powell        11.99
Churandy Martina     9.94
Justin Gatlin        9.79
Richard Thompson     9.98
Ryan Bailey          9.88
Tyson Gay            9.80
Usain Bolt           9.63
Yohan Blake          9.75
Superman             5.00
Batman               6.00
dtype: float64
>>> r[r<9] = 1.0
>>> r
Asafa Powell        11.99
Churandy Martina     9.94
Justin Gatlin        9.79
Richard Thompson     9.98
Ryan Bailey          9.88
Tyson Gay            9.80
Usain Bolt           9.63
Yohan Blake          9.75
Superman             1.00
Batman               1.00
dtype: float64
>>> print ('Ironman' in r)
False
>>> print ('Superman' in r)
True
>>> print ('Milkha Singh' in r)
False
>>> 

```

Addition of two Series 

```
>>> new_r = pd.Series({'Lalita Baber': 15.0,  'O P Jaisha': 16.0, 'Kavita Raut': 20.0, 'Usain Bolt':9.63,  'Milkha Singh':None})
>>> new_r.isnull()
Kavita Raut     False
Lalita Baber    False
Milkha Singh     True
O P Jaisha      False
Usain Bolt      False
dtype: bool
>>> new_r.notnull()
Kavita Raut      True
Lalita Baber     True
Milkha Singh    False
O P Jaisha       True
Usain Bolt       True
dtype: bool
>>> 

```

### Practice on Series

* For dictionary for High Protein Fruits
100gm 
```

Fruit,Protein,Fat,Calories,Carbs
Dried Apricots,3.39,0.51,241,62.64
Raisins,4.45,0.67,434,114.81
Guava,2.3,0.86,61,12.89
Dates,0.2,0.03,23,6.23
Avocado,4.02,29.47,322,17.15

```
 


## DataFrames

```
>>> data = {'name':['Usain Bolt','Yohan Blake','Justin Gatlin','Tyson Gay','Ryan Bailey','Churandy Martina','Richard Thompson','Asafa Powell'],
...         'speed':[9.63,9.75,9.79,9.8,9.88,9.94,9.98,11.99],
...         'height':[76.77,70.86,72.83,70.07,75.98,70.07,70.01,70.8],
...         'weight':[209.439,167.551,182.984,165.347,216.053,163.142,176.37,191.802]}
>>> 
>>> data
{'speed': [9.63, 9.75, 9.79, 9.8, 9.88, 9.94, 9.98, 11.99], 'name': ['Usain Bolt', 'Yohan Blake', 'Justin Gatlin', 'Tyson Gay', 'Ryan Bailey', 'Churandy Martina', 'Richard Thompson', 'Asafa Powell'], 'height': [76.77, 70.86, 72.83, 70.07, 75.98, 70.07, 70.01, 70.8], 'weight': [209.439, 167.551, 182.984, 165.347, 216.053, 163.142, 176.37, 191.802]}
>>> 

```

Reading from CSV File. 

```

>>> food = pd.read_csv("food.csv")
>>> food
                      Food  Index  Calories  Cholesterol  Total_Fat  Sodium  \
0          Frozen Broccoli      1      73.8          0.0        0.8    68.2   
1              Carrots,Raw      2      23.7          0.0        0.1    19.2   
2              Celery, Raw      3       6.4          0.0        0.1    34.8   
3              Frozen Corn      4      72.2          0.0        0.6     2.5   
4      Lettuce,Iceberg,Raw      5       2.6          0.0        0.0     1.8   
5      Peppers, Sweet, Raw      6      20.0          0.0        0.1     1.5   
6          Potatoes, Baked      7     171.5          0.0        0.2    15.2   
7                     Tofu      8      88.2          0.0        5.5     8.1   
8          Roasted Chicken      9     277.4        129.9       10.8   125.6   
9       Spaghetti W/ Sauce     10     358.2          0.0       12.3  1237.1   
10     Tomato,Red,Ripe,Raw     11      25.8          0.0        0.4    11.1   
11        Apple,Raw,W/Skin     12      81.4          0.0        0.5     0.0   
12                  Banana     13     104.9          0.0        0.5     1.1   
13                  Grapes     14      15.1          0.0        0.1     0.5   
14     Kiwifruit,Raw,Fresh     15      46.4          0.0        0.3     3.8   

```

