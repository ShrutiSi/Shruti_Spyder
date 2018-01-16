# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:13:37 2017

@author: saach
"""

help(round)

import numpy as np
height = [1.73,1.68,1.71,1.89,1.79]
weight = [65.4,59.2,63.6,88.4,68.7]

np_height= np.array(height)
np_weight=np.array(weight)
np_bmi= np.round(np_weight/np_height**2,2)
print(np_bmi)
bmi = height+weight
print(bmi)
np_bmi1= np_height+np_weight
print(np_bmi1)

np_bmi>23
np_bmi[np_bmi>23]

x= int(input("Enter value of x"))
if x==3:
    print("x equals 3")
elif x==2:
    print("x equals 2")
else:
    print("x equals something else")
print("this is outside the if ")

for somechar in "Hello World":
    print (somechar)
    
for study in "PYTHON":
    print (study)
    
for (x,y) in [('a',1), ('b',2),('c',3),('d',4)]:
    print (x)
    print(y)
    
for weekday in ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday']:
    print(weekday)
    
for z in range(50):
    print (z)
    
x = [1,2,3,4,5,6]
for x in x:
    print(x+5)
    
numbers = [1,2,3,4,5,6]
for x in numbers:
    if x in [2,3,4,5]:
        x=x+5
    print(x)
    
numbers = [1,2,3,4,5,6]
for x in numbers:
    x+=5
    print(x)
       
numbers = [1,2,3,4,5,6]
for x in numbers:
    if x%2==0:
        x=x+5
    print(x)

x=3
while x<10:
    x =x+1
    print ("Still in the loop")
print("Outside of the loop")

x=3
while x>10:
    x =x+1
    print ("Still in the loop")
print("Outside of the loop")

while 1:
    print ("Type Ctrl-C to stop me")

x= 'spam'
while x:
    print (x)
    x= x[1:]
    
while 1:
    name = input('Enter name:')
    if name == 'stop':
        break
    age = input('Enter age:')
    print ('Hello', name, '=>', \
    int(age)**2)
    
x = 10
while x:
    x = x-1
    if x%2 !=0: continue
    print(x)
    


print(1 or 0) 
print(100 and 50)  

def myfun(b, c):
        return b+c
myfun(3,4)
    
def hello():
  name = str(input("Enter your name: "))
  if name:
      print ("Hello" + str(name))
  else:
      print("Hello world")
      return
hello()

def hello():
  name = str(input("Enter your name: "))
  age = input("Enter your age: ")
  if name:
      print ("Hello" + str(name))
      print("Age is " + age)
  else:
      print("Hello world")
      return
hello()

def intersect(seq1, seq2):
    res= []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
print(intersect('neena','meena'))
print(intersect('karan', 'Polam'))

