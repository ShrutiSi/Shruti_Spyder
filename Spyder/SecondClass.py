# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

c="aa"+"bb"

counter = 1 

def doLotsOfStuff():
    
    global counter

    for i in (1, 2, 3): 
        counter += 1

doLotsOfStuff()

print(counter)

%%timeit
L = []
for n in range(1000):
    L.append(n**2)