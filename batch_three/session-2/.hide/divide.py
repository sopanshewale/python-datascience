#!/usr/bin/python3

one = int(input("Enter First Number:"))
two = int(input("Enter Second Number:"))

try: 
    div = one/two  
    print ("The division is: ", div)
except ZeroDivisionError:
    print ("You tried to divide", one, "by zero")


