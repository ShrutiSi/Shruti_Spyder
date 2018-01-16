# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:49:26 2017

@author: saach
"""
# when u want to check an exceptional error, we can use Try command as given below
try:
    fh = open("testfile.txt", "w")
    fh.write("This is my test file for exception handling!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close
    
import os
os.getcwd()

import time; # to find the seconds from a particular date
ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print ("local current time: ", localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localti
      
      me.tm_mday)
# to get the local time use asctime function
localtime = time.asctime(time.localtime(time.time()))
print ("Local Current time: " , localtime)

#to get the calendar
import calendar
cal = calendar.month(2008,5)
print("Here is a calendar:")
print (cal)

#to get date time
import datetime
today = datetime.date.today()
print("Today :", today)
yesterday = today - datetime.timedelta(days =1)
tomorrow = today + datetime.timedelta(days =1)
print(yesterday)
print(tomorrow)

# to find the number of days between two dates
from datetime import date
a = date(2016,1,31)
b = date(2017,1,31)
print(b-a)

# 30102017
"""Pandas"""
import numpy
randn = numpy.random.randn
from pandas import *
s= Series(randn(3),('a','b','c'))
print(s)
print(s.mean())

a= randn(30)
print(a)
print(s.index)
s=s.reindex(['c','b','a'])
print(s)
s+s
numpy.exp(s) #exponential
""" Dataframe"""
d = {'one':s*s, 'two': s+s}
df = DataFrame(d)
print(df)
df.index
df.columns
df.values # values used for rows
df['three'] = s*3
print(df)
df.one # access
sum(df.one)
df.drop('c')
df.drop('three', axis =1)
df.mean()
df.median()

s1=Series(randn(1000))
s2=Series(randn(1000))
print(s1.cov(s2))
print(s1.corr(s2))
print(s1.corr(s2,method = 'spearman'))
?randn
randn.seed(1000)
