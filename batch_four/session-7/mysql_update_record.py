#!/usr/bin/python3
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
def update_presidents(president_id, name):
    # read database configuration
    db_config = read_db_config()
 
    # prepare query and data
    query = """ UPDATE presidents 
                SET name = %s
                WHERE id = %s """
 
    data = (name, president_id)
 
    try:
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
 
    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()
if __name__ == '__main__':
    update_presidents(3, 'George Bush')
