#!/usr/bin/python3

name = "Hari Sadu"

def hellofunction(name=None):
    '''This is demonstration to define function. 
       The function is not very great'''
    if name:
       print ("Hello " + name )
    else: 
      print ("Hello World!")

print (hellofunction.__doc__)

