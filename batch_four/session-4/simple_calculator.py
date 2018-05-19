#!/usr/bin/python3
# Task: Complete  Simple Calculator

def add (m, n):
   """This function adds two numbers"""
   return m + n


def subtract(): 
   """This function subtracts two numbers"""
   pass 

def multiply(): 
   """This function multiplies two numbers"""
   pass 

def divide(): 
   """This function divides two numbers"""
   pass 

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1': 
     answer = add(num1, num2)
     print (answer)

