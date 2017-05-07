
```

>>> import pandas as pd
>>> raw_data = { 
...              'subject': ['1', '2', '3', '4', '5'],
...              'first_name': ['Michel', 'Mark', 'Matt', 'Ryan', 'Gary'],
...              'last_name': ['Phelps', 'Spitz', 'Biondi', 'Lochte', 'Hall']
...            }
>>> 
>>> raw_data
{'subject': ['1', '2', '3', '4', '5'], 'first_name': ['Michel', 'Mark', 'Matt', 'Ryan', 'Gary'], 'last_name': ['Phelps', 'Spitz', 'Biondi', 'Lochte', 'Hall']}
>>> df_a = pd.DataFrame(raw_data, columns = ['subject', 'first_name', 'last_name'])
>>> df_a
  subject first_name last_name
0       1     Michel    Phelps
1       2       Mark     Spitz
2       3       Matt    Biondi
3       4       Ryan    Lochte
4       5       Gary      Hall
>>> 


```


and second set

```

>>> raw_data = {
...             'subject': ['4', '5', '6', '7', '8', '9'],
...             'first_name': ['Ian', 'Aaron', 'Nathan', 'Tom', 'Don', 'Johny'],
...             'last_name': ['Thorpe', 'Peirsol', 'Adrian', 'Jager', 'Schollander', 'Weis'] 
...            }
>>> df_b = pd.DataFrame(raw_data, columns = ['subject', 'first_name', 'last_name'])
>>> df_b
  subject first_name    last_name
0       4        Ian       Thorpe
1       5      Aaron      Peirsol
2       6     Nathan       Adrian
3       7        Tom        Jager
4       8        Don  Schollander
5       9      Johny         Weis
>>> 


```


Third one 

```

>>> raw_data = {
...             'subject': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
...             'test'   : [51, 15, 15, 61, 16, 14, 15, 1, 61, 16] 
...            }
>>> df_n = pd.DataFrame(raw_data, columns = ['subject','test'])
>>> df_n
  subject  test
0       1    51
1       2    15
2       3    15
3       4    61
4       5    16
5       7    14
6       8    15
7       9     1
8      10    61
9      11    16
>>> 

```

Join dataframes on rows

```
>>> df_new = pd.concat([df_a, df_b])
>>> df_new
  subject first_name    last_name
0       1     Michel       Phelps
1       2       Mark        Spitz
2       3       Matt       Biondi
3       4       Ryan       Lochte
4       5       Gary         Hall
0       4        Ian       Thorpe
1       5      Aaron      Peirsol
2       6     Nathan       Adrian
3       7        Tom        Jager
4       8        Don  Schollander
5       9      Johny         Weis
>>> 

```

Join along axis

```
>>> pd.concat([df_a, df_b], axis=1)      
  subject first_name last_name subject first_name    last_name
0       1     Michel    Phelps       4        Ian       Thorpe
1       2       Mark     Spitz       5      Aaron      Peirsol
2       3       Matt    Biondi       6     Nathan       Adrian
3       4       Ryan    Lochte       7        Tom        Jager
4       5       Gary      Hall       8        Don  Schollander
5     NaN        NaN       NaN       9      Johny         Weis
>>> 

```

Merge 

```

>>> pd.merge(df_new, df_n, on='subject')
  subject first_name    last_name  test
0       1     Michel       Phelps    51
1       2       Mark        Spitz    15
2       3       Matt       Biondi    15
3       4       Ryan       Lochte    61
4       4        Ian       Thorpe    61
5       5       Gary         Hall    16
6       5      Aaron      Peirsol    16
7       7        Tom        Jager    14
8       8        Don  Schollander    15
9       9      Johny         Weis     1
>>> 

```


```
>>> pd.merge(df_new, df_n, left_on='subject', right_on='subject')
  subject first_name    last_name  test
0       1     Michel       Phelps    51
1       2       Mark        Spitz    15
2       3       Matt       Biondi    15
3       4       Ryan       Lochte    61
4       4        Ian       Thorpe    61
5       5       Gary         Hall    16
6       5      Aaron      Peirsol    16
7       7        Tom        Jager    14
8       8        Don  Schollander    15
9       9      Johny         Weis     1
>>> 

```

outer merge

```
>>> pd.merge(df_a, df_b, on='subject', how='outer')
  subject first_name_x last_name_x first_name_y  last_name_y
0       1       Michel      Phelps          NaN          NaN
1       2         Mark       Spitz          NaN          NaN
2       3         Matt      Biondi          NaN          NaN
3       4         Ryan      Lochte          Ian       Thorpe
4       5         Gary        Hall        Aaron      Peirsol
5       6          NaN         NaN       Nathan       Adrian
6       7          NaN         NaN          Tom        Jager
7       8          NaN         NaN          Don  Schollander
8       9          NaN         NaN        Johny         Weis
>>> 

```

Inner Join 

```
>>> pd.merge(df_a, df_b, on='subject', how='inner')
  subject first_name_x last_name_x first_name_y last_name_y
0       4         Ryan      Lochte          Ian      Thorpe
1       5         Gary        Hall        Aaron     Peirsol
>>> 

```


Left and Right joins


```
>>> pd.merge(df_a, df_b, on='subject', how='right')
  subject first_name_x last_name_x first_name_y  last_name_y
0       4         Ryan      Lochte          Ian       Thorpe
1       5         Gary        Hall        Aaron      Peirsol
2       6          NaN         NaN       Nathan       Adrian
3       7          NaN         NaN          Tom        Jager
4       8          NaN         NaN          Don  Schollander
5       9          NaN         NaN        Johny         Weis
>>> pd.merge(df_a, df_b, on='subject', how='left')
  subject first_name_x last_name_x first_name_y last_name_y
0       1       Michel      Phelps          NaN         NaN
1       2         Mark       Spitz          NaN         NaN
2       3         Matt      Biondi          NaN         NaN
3       4         Ryan      Lochte          Ian      Thorpe
4       5         Gary        Hall        Aaron     Peirsol
>>> 

```

On the basis of indexes

```
>>> pd.merge(df_a, df_b, right_index=True, left_index=True)
  subject_x first_name_x last_name_x subject_y first_name_y  last_name_y
0         1       Michel      Phelps         4          Ian       Thorpe
1         2         Mark       Spitz         5        Aaron      Peirsol
2         3         Matt      Biondi         6       Nathan       Adrian
3         4         Ryan      Lochte         7          Tom        Jager
4         5         Gary        Hall         8          Don  Schollander
>>> 

```

