"""Defining like this sets a defult paramter for
    y if 1 is not given, its custom to not use 
    spaces here between the ='s"""
#Defult paramaters must be put at end before all required.

def add(x,y=8):
    print(x + y)

add(5)



default_y = 3

def addExample2(x, y=default_y):
    sum = x + y
    print(sum)

addExample2(2)

'''Changing the default value after the function has already
    been created will not change the defualt within the function;
    they become static.'''
#This will not make a diffrence    
default_y = 4
addExample2(2)