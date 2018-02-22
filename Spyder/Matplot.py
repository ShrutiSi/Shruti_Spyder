# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:25:00 2018 by Shruti Sinha
"""

import matplotlib as mp1
import matplotlib.pyplot as plt
plt.style.use('classic')

import matplotlib.pyplot as plt
import numpy as np
x =np.linspace(0,10,100)
plt.plot(x, np.sin(x))
plt.plot(x,np.cos(x))
plt.show()
%matplotlib inline
plt.draw

x=np.linspace(0,10,100)
x
fig = plt.figure()
plt.plot(x,np.sin(x), '-')
plt.plot(x,np.cos(x),'--')
fig.savefig('myfigure.png')
!dir *.png

plt.subplot(2,1,1)
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x,np.cos(x))

fig, ax=plt.subplots(3)
ax[0].plot(x, np.sin(x))
ax[1].plot(x,np.cos(x))
ax[2].plot(x,np.tan(x))

fig = plt.figure()
ax=plt.axes()
x = np.linspace(0,10,100)
ax.plot(x,np.sin(x))

plt.plot(x, np.sin(x-1), color = 'g', linestyle= 'solid', label = 'sin(x)')
plt.plot(x, np.sin(x-2), color= '0.75', linestyle= 'dashed', label = 'sin(x1)')
plt.plot(x,np.sin(x-3), color ='#FFDD44', linestyle= 'dotted', label = 'sin(x2)')
plt.legend();

