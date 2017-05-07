#!/usr/bin/python3
import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

new_db = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
    if new_db:
        print('Let us create schema')
        with open(schema_filename, 'r') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.executescript("""
        insert into project (name, description, deadline)
        values ('assignments', 'Assignments - Python for Data Science', '2017-05-24');

        insert into task (details, status, deadline, project)
        values ('assignment 1', 'done', '2017-01-29', 'assignments');

        insert into task (details, status, deadline, project)
        values ('assignment 2', 'in progress', '2017-02-22', 'assignments');

        insert into task (details, status, deadline, project)
        values ('assignment 3', 'active', '2017-03-31', 'assignments');
        """)
    else:
        print('Database exists, assume schema does, too.')
