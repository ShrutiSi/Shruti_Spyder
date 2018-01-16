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
