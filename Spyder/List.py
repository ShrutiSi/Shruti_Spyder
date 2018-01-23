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
