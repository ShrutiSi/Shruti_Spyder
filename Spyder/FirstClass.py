# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:58:14 2017

@author: saach
"""

def addtwonos(x,y):
    print(x+y)
    
addtwonos(3, 5)
addtwonos(-10, -22)

fam = [1.73,1.68,1.71,1.89]
print(fam)

print(fam+fam)
print(fam*3)

fam = ['liz', 1.73, 'emma',1.68, 'mom', 1.71, 'dad', 1.89 ]
print(fam)
type(fam)
fam[3]
fam[-1]
fam[3:5]
fam[0:2] = ['lisa', 1.84, 'emma']
print(fam)
fam_ext = fam + ['me', 1.79]
print(fam_ext)
del(fam_ext[2])
print(fam_ext)

x = ["a","b","c"]
y = x

y[1] = "z"
print(y)
print(x)


y = list(x)
y[1] = "e"
print(y)
print(x)

