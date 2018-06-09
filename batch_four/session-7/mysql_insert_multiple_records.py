#!/usr/bin/python3

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def insert_presidents(presidents):
    query = "INSERT INTO presidents(name,age) " \
            "VALUES(%s,%s)"
 
    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)
 
        cursor = conn.cursor()
        cursor.executemany(query, presidents)
 
        conn.commit()
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
 
def main():
   presidents = [ ('A', 10), ('B', 20), ('C', 30)]
   insert_presidents(presidents)
 
if __name__ == '__main__':
    main()

