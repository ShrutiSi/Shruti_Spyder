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

# Dictionary
d = {'user':'bozo', 'pswd': 1234 }
d['user']
d['id'] = 45
d
d['valid']= "31.03.2020"
d
del d['valid'] # remove one
d
d.clear() # remove all
d = {'user': 'bozo', 'p':1234, 'i':34}
d.keys()
d.values()
d.items()
print("my userid is", d['user'] , 'ans my password is' , d['p'] )
len(d) #length of keys
d1 = {'class':'syntax','room':'ecme107', 'i':55}
d.update(d1)
d #dictionary keys are unique

import numpy as np
a= np.array([1,3,5,7,9])
b= np.array([3,5,6,7,9])
c = a+b
print (c)
type(c)
c.shape

a=np.array([0,1,2,3])
a
np.shape(a)
a.ndim
list(a)
b =a.copy()
,
de,f numb,er(x,y):
 ,   ,n,,umber,= (x+y)
  ,  print(number)
number(3,4)

num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")
   
def diff21(x):
    if x>21:
        result = 2*(x-21)
    else:
        result = 21-x
    return result
diff21(31)

def diff21(n):
    if n>21:
        result = 2*(n-21)
    else:
        result = 21-n
    return result
def sum_double(x,y):
    if x==y:
        sum = 2*(x+y)
    else:
        sum = x+y
    return sum
sum_double(1,2)

def missing_char(str, n):
    return str[0:n] + str[n+1:]
missing_char('kitten',4)

,,import, m,atplotlib.pyplot as plt
year = [1,950, 1970, 1990, 2010]
pop = [2.519, 3.692,5.263,6.972]
year =[1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop
plt.plot(year,pop)
plt.show()
plt.scatter(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('world population')
plt.yticks([0,2,4,6,8,10],['0', '2B', '4B', '6B','8B','10B'])
plt.show()

help(plt.hist)
values= [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values)
plt.show()
plt.hist(values, bins =4)
plt.show()
#Multiple graphs with single command
import numpy as np
t = np.arange(0., 5., 0.2)
plt.plot(t,t,'r--', t,t**2, 'bs',t,t**3, 'g^')
plt.axis([0,6,0,150]) # x and Y range of axis
plt.show()
#Generate a normal distribution
mu,sigma = 100,15
x = mu +sigma *np.random.randn(10000)
plt.hist(x,50, ormed = 1,facecolor = 'g')
plt.xlabel('smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60,.025,r'$\mu=100, \\sigma=15$')
plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()

data1 =[49,66,24,98,37,64,98,27,56,93,68,78,22,25,11]
def mean(data):
    return(sum(data)/len(data))
print(mean(data1))

def median(data):
    l1 = sorted(data)
    x = len(data)
    if (x%2==0):
        median =(l1[(x//2)-1]+l1[(x//2)])/2
    else:
        median = l1[(x-1)//2]
    return(median)
data2 = [1,2,5,10,-20,30]
median(data2)

def mode(array):
    most = max(list(map(array.count, array)))
    return list(set(filter(lambda x: array.count(x) == most, array)))
data3 = [1,1,2,2,3,3,4,4,4,4,5,6]
mode(data3)

def ss(data):
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss
ss(data1)

def stddev(data, ddof=0):
    n = len(data)
    if n < 2:
        raise ValueError
    ss = ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5
stddev(data1)
from math import sqrt
def stddev(lst):
    mn = mean(lst)
    variance = sum([(e-mn)**2 for e in lst]) / len(lst)
    return sqrt(variance)
stddev(data1)