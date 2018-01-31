# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:52:10 2018 by Shruti Sinha
"""

import os
import sys
os.path.dirname(sys.executable)
import keyword
print(keyword.kwlist)
a=b=c=1
a
b
c
a,b,c = 1,2,"Tom"
print(a,b,c)
for i in range(4):
    print(i, i+2, sep = '&', end = '-' )
    print(i+2)
    for j in range(3):
        print(j, end = ' ')
        
first = 1
second = 2
third = 3
gtotal = first +\
second +\
third 
gtotal
n = input ("Enter a number")
n +2
m = eval(input("Enter a number"))
m
"""%reset - it is to remove the variables"""

l =[1,2,"a"]
"""List is mutable, can be changed"""
type(l)
tuple = (1,2,"a") 
"""Tuple is same as list except that it is immutable, plus it is faster and consume less energy"""
type(tuple)
D = {"a":1, "b":2}
type(D)
"""Dictionary is mutable"""
S1 = {1,2,3}
type(S1)
"""Set is unique values, unordered, no indexing/slicing; changes can be done"""
fs=frozenset({1,2,3})
type(fs)
""" frozen set is fixed cannot be changed but other properties are like set"""

l= [1,2,3]
for i in range(len(l)):
    print(l[i], end = ',')
          

def square(a):
    """ This will square the value"""
    return(a**2)
square(3)


import numpy as np
