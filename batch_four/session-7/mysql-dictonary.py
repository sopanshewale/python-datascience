#!/usr/bin/python3
import mysql.connector  

config = {
  'user': 'root',
  'password': 'welcome123',
  'host': '127.0.0.1',
  'database': 'mysql',
  'raise_on_warnings': True,

}

# Open database connection
db = mysql.connector.connect(**config)
#db = mysql.connector.connect(user='root', password='welcome123', host='localhost', database='mysql')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute('SELECT VERSION()')

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : {} ".format( data))

# disconnect from server
db.close()

