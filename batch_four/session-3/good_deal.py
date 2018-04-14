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

