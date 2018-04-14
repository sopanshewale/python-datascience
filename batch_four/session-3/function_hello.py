#!/usr/bin/python3

name = "Hari"

def hellofunction(name=None):
    '''hello function'''
    if name:
       print ("Hello " + name )
    else: 
      print ("Hello World!")

#hellofunction(name)
hellofunction('Hari Sadu')
#hellofunction()

