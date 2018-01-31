# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:52:28 2018 by Shruti Sinha
"""

rollnos = [1,2,3,4,5,6,10,11]
rollnos[1]
len(rollnos)
sum(rollnos)
min(rollnos)
max(rollnos)
rollnos
for i in range(len(rollnos)):
    print(rollnos[i], end=",")
    
if 3 in rollnos:
    print("Yes")
else:
    print("No")
    

rollnos.append(13)
rollnos
sorted(rollnos)
rollnos.index(13)
rollnos.append(12)

a = 'ls'
b = 'nice'
my_list = ['my','list',a,b]
my_list2 = [[4,5,6,7], [3,4,5,6]]
my_list[1]
my_list[-3]
my_list[1:3]
my_list[-len(my_list)]
len(my_list)
my_list[1:]
my_list[:3]
my_list[:]
my_list2[1][0]
my_list2[0][1]
my_list2[1][:2]
my_list*2
my_list2[1][0]>4
my_list.index(a)
my_list.count(a)
my_list.append('l')
my_list
my_list.extend('!')
my_list.remove('!')
my_list.sort()
