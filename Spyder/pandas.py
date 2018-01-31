# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:16:25 2018 by Shruti Sinha
"""
import numpy as np
import pandas as pd
pd.__version__
data = pd.Series([0.25,0.5,0.75,1.0])
data
data.values
data.index
data[1]
data = pd.Series([0.25, 0.5,0.75,1.0], index = ['a','b','c','d'])
data
population_dic = {'cal': 35268, 'tex':85214, 'Ny':78955, 'Flr':85214, 'Illin':789654}
population = pd.Series(population_dic)
population
area = [5214,6541,2541,96584,58214]
states = pd.DataFrame({'population':population, 'area':area})
states

rollno = [1,2,3,4]
name = ['a','b','c', 'd']
marks = [20,30,40,50]
df1 = pd.DataFrame({'name':name,'rollno':rollno,'marks':marks}, columns = ['name','rollno','marks'])
df1
foobar = np.random.rand(3,2)
foobar
fobar = pd.DataFrame(np.random.rand(3, 2),columns=['foo', 'bar'],index=['a', 'b', 'c'])
fobar
data.iloc[1]
data.iloc[1:3]
data.loc['a']
states['area']
states.area
states.values[0]
