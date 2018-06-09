#!/usr/bin/python3
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def query_with_fetchmany():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
 
        cursor.execute("SELECT * FROM presidents")
 
        for row in iter_row(cursor, 10):
            print(row)
 
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()

 
if __name__ == '__main__':
    query_with_fetchmany()



