```
$ sqlite3 
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .help
.auth ON|OFF           Show authorizer callbacks
.backup ?DB? FILE      Backup DB (default "main") to FILE
sqlite> 




sqlite> .schema
sqlite> 
sqlite> CREATE TABLE presidents(
   ...> id int primary key NOT NULL,
   ...> name char(100) NOT NULL,
   ...> age int NOT NULL
   ...> );

sqlite> .schema
CREATE TABLE presidents(
id int primary key NOT NULL,
name char(100) NOT NULL,
age int NOT NULL
);

sqlite> select id, name, age from presidents;
sqlite> select * from presidents;



sqlite> INSERT INTO presidents (id, name, age) values (1, 'Donald T', 75);
sqlite> select id, name, age from presidents;
1|Donald T|75


sqlite> select * from presidents;
1|Donald T|75
sqlite> 

sqlite> INSERT INTO presidents (id, name, age) values (2, 'Barack O', 54);

sqlite> select * from presidents;
1|Donald T|75
2|Barack O|54

sqlite> select * from presidents where id=2;
2|Barack O|54
sqlite> select * from presidents ORDER BY age;
2|Barack O|54
1|Donald T|75
sqlite> 



>>> conn = sqlite3.connect('example.db')
>>> type(conn)
<class 'sqlite3.Connection'>
>>> c = conn.cursor()
>>> type(c)
<class 'sqlite3.Cursor'>
>>> c.execute(
...            '''CREATE TABLE stocks
...                 (date text, trans text, symbol text, qty real, price real) 
...            '''
...          )
<sqlite3.Cursor object at 0x10b1f8f80>
>>> c.execute("INSERT INTO stocks VALUES('2018-01-05', 'BUY', 'GOOG', 100, 34.50)")
<sqlite3.Cursor object at 0x10b1f8f80>
>>> conn.commit()
>>> conn.close()
>>> 
>>> 
>>> 
$ 
$ 
$ ls -al
total 24
drwxr-xr-x   4 sopanshewale  staff   136 Jun  8 20:04 .
drwxr-xr-x  22 sopanshewale  staff   748 Jun  8 19:41 ..
-rw-r--r--   1 sopanshewale  staff  1163 Jun  8 19:56 README.md
-rw-r--r--   1 sopanshewale  staff  8192 Jun  8 20:04 example.db
$ sqlite3 example.db 
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real);
sqlite> select * from stocks;
2018-01-05|BUY|GOOG|100.0|34.5
sqlite> 

```
