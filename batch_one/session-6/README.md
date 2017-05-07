**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Interacting with Data](#)
	- [JSON](#)
		- [Demonstrate](#)
	- [Interacting with Files](#)
		- [Open() function](#)
	- [Getting data from Internet](#)
		- [Demonstrate](#)

# Interacting with Data 

* Every software tool deals with the data
* The data is taken as input to the software tool
** After doing some crunching-be cleaning of data, be it adding meta-data to the data
** It leads to generate new data
* The new data is sent to other destination for the consumption - consumption can be input to other tools 

Python also deals with data - Python Programming has libraries to deal with  

* Filesystem based data
* Databases 
* Internet based 
* ... 

## JSON

JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language

JSON is a text format that is completely language independent 

JSON is built on two structures:

* A collection of name/value pairs  - similar to dictionary, hash table
* An ordered list of values -  similar to list

Look at a few examples: 

```
{
    "id": 1,
    "name": "A green door",
    "price": 12.50,
    "tags": ["home", "green"]
}

```

Another one: 

```
{
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}
```

### Demonstrate 

```
#!/usr/bin/python3
import json

data = [
         {
             'a': 'AAA', 
             'b': (1, 2, 3, 4, 5), 
             'c': 78.0}

       ]

print (type(data))
print (data)

json_data = json.dumps(data)
print (type(json_data))
print (json_data)



back_to_data = json.loads(json_data)
print(type(back_to_data))
print (back_to_data)

```

The execution looks as below:

```
# ./simple_json.py 
<class 'list'>
[{'c': 78.0, 'a': 'AAA', 'b': (1, 2, 3, 4, 5)}]
<class 'str'>
[{"c": 78.0, "a": "AAA", "b": [1, 2, 3, 4, 5]}]
<class 'list'>
[{'c': 78.0, 'a': 'AAA', 'b': [1, 2, 3, 4, 5]}]

```

Look at the following - nicely formated output: 

```
#!/usr/bin/python3
import json

data = [
         {
             'a': 'AAA', 
             'b': (1, 2, 3, 4, 5), 
             'c': 78.0}

       ]

print(json.dumps(data, sort_keys=True, indent=2))

```


## Interacting with Files 

### Open() function 

```
file_object  = open(“filename”, “mode”) 
```

Mode is one of the following:

* ‘r’ – Read mode which is used when the file is only being read 
* ‘w’ – Write mode which is used to edit and write new information to the file (any existing files with the same name will be erased when this mode is activated) 
* 'a’ – Appending mode, which is used to add new data to the end of the file; that is new information is automatically amended to the end 
* ‘r+’ – Special read and write mode, which is used to handle both actions when working with a file 

Let us create new file with some content:

```
#!/usr/bin/python3
#simple_file_creation.py
f = open ('simple_data.txt', 'w')

f.write("Hello to writing data into file")
f.write("Line ------2")
f.write("Line ------3")
f.close()

```

To read - you can use: 

```
file.read() 
```

check following:

```
#!/usr/bin/python3
#simple_file_read.py

f = open('simple_data.txt', 'r')

print (f.read())
f.close()

```

Look at another code:

```
#!/usr/bin/python3
# read_line.py 
 
f = open('data.txt', 'r')

for l in (f.readlines()):
   print (l)

```

Demostrate another one: 

```
#!/usr/bin/python3

def do_stuff_that_fails():
     print("I actually failed to work")

def do_stuff_when_it_doesnt_work():
     print("Tried but it did not work")

try:
    with open('my_file_which_do_not_exist') as f:
        read_data = f.read() 
        print (read_data)

        do_stuff_that_fails()
except (IOError, OSError) as e:
    do_stuff_when_it_doesnt_work()

```


## Getting data from Internet 

### Demonstrate 

```
#!/usr/bin/python3
import urllib.request
import time

stocks_to_pull = ['AMD', 'BAC', 'MSFT', 'TXN', 'GOOG']

def pull_data_for_stock(stock):
    stock_file = stock + '.txt'
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
    print ("Data from URL: " + url)
    with urllib.request.urlopen(url) as f:
        source = f.read().decode('utf-8')
   
    split_source = source.split('\n')

    for line in split_source:
        #print (line) 
        splitLine = line.split(',') # <---(here ',' instead of '.')
        if len(splitLine) == 6: # <----( here, 6 instead of 5 )
            if 'values' not in line: 
                saveFile = open(stock_file,'a')
                linetoWrite = line+'\n'
                saveFile.write(linetoWrite)

    print('Pulled', stock)
    print('...')
    time.sleep(.5)

if __name__=="__main__":
    for stock in stocks_to_pull: 
        print ("working on " + stock)    
        pull_data_for_stock(stock)

```


