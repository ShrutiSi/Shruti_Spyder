# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:04:22 2018 by Shruti Sinha
"""

import numpy as np
import pandas as pd
rollnoL = [109, 102, 105, 106, 103, 110, 101, 107,104, 111, 108]
nameL = ['meena', 'apporva','kaustav','shubham', 'Goldie', 'hitesh', 'shruti','vijay', 'achal','lalit','varun']
genderL = ['F','F','M','M','M','M','F','M','M','M','M']
pythonL = np.random.randint(60,90,11)
sasL = np.random.randint(50,95,11)
nameS = pd.Series(nameL, index = rollnoL)
nameS
# convert series to index#
list(nameS.items()) 
nameS[108] = 'jain'
nameS
nameS[nameS == "jain"]
nameS[0:5]
nameS[101:106] # wrong#
nameS.iloc[0:5]
nameS.loc[108]
# difference between iloc and loc, when i is used then it is implicit indexing whereas without i it is user defned#
nameS == 'meena'
nameS.iloc[4:6]
nameS.loc[103:110] #explicit indexing#
nameS.ix[108]
nameS.loc[108]
nameS = pd.Series(nameL)
rollnoS = pd.Series(rollnoL)
genderS = pd.Series(genderL)
pythonS = pd.Series(pythonL)
sasS = pd.Series(sasL)
studentDF1 = pd.concat([rollnoS,nameS,genderS,pythonS,sasS],axis =1)
#dictionary method to create a dataframe#
studentDF1 = pd.DataFrame({'rollno':rollnoL,'name':nameL,'gender':genderL,'python':pythonL, 'sas':sasL})
#this will help in creating the dataframe with the column in the order it is mentioned#
studentDF1 = pd.DataFrame({'rollno':rollnoL,'name':nameL,'gender':genderL,'python':pythonL, 'sas':sasL}, columns = ['rollno', 'gender','name','python','sas'])
studentDF1.values
studentDF1.T #transpose#
studentDF1.iloc[1:3]
studentDF1.iloc[:3,:2]
studentDF1.loc[:5,:'python']
studentDF1.iloc[:5,:2]
studentDF1['Total'] = studentDF1['sas'] + studentDF1['python']
studentDF1[Total  > 150]
courseL = ['pg','pg','msc','msc','pg','pg','pg','pg','pg','pg','bsc']
hadoopL = np.random.randint(71,90,11)
feesL = np.random.randint(100000,150000,11)
hostelL = [True,False,True,False,False,True,False,True,True,True,False]

studentDF = pd.DataFrame({'rollno':rollnoL,'name':nameL,'gender':genderL,'python':pythonL, 'sas':sasL,'course':courseL,'hadoop':hadoopL,'fees':feesL,'hostel':hostelL}, columns = ['rollno' ,'name','gender','python','sas','hadoop','fees','course', 'hostel'])
studentDF
studentDF['Total']= studentDF['sas']+studentDF['python']+studentDF['hadoop']

#write a csv file
studentDF.to_csv("student2.csv")

studentDF.columns
studentDF.groupby('gender').mean()
studentDF.groupby('gender').size()
studentDF.groupby(['gender','course'])['hostel' ].aggregate('mean').unstack()
from numpy import random
classes = ['c1','c2','c3']
sclass = random.choice(classes,11)
sclass
studentDF['class'] = pd.Series(sclass)
pd.pivot_table(studentDF, index = ['name'])
pd.pivot_table(studentDF, index = ['name','class','hostel'])
pd.pivot_table(studentDF, index = ['class', 'gender'])
pd.pivot_table(studentDF, index = ['course','class'], values= ['Total','python'])
pd.pivot_table(studentDF, index = ['course','class'], values= ['Total','python'], aggfunc=np.sum)
pd.pivot_table(studentDF, index = ['course','class'], values= ['Total','python'],aggfunc = [np.sum,np.mean,len])

## random seed##
rng = np.random.RandomState(42)
rng
marks = pd.Series(rng.randint(50,100,11))

marks.sum()
marks.std
dict(x=1, y=4)
dict(x=1, y=[1,2])

A = pd.Series(rng.randint(1,10,6))
B = pd.Series(rng.randint(1,10,6))
df = pd.concat([A,B], axis =1)
df
df.columns = ['A','B']
df
df.mean()
df.mean(axis=0)
df.mean(axis = 'rows')
df.mean(axis =1)
df.mean(axis = 'columns')
df.describe()
df.groupby(['A']).sum()

['A','B','C']*2
np.repeat(['A','B','C'],2)
np.repeat(['A','B','C'],[1,2,3])

df = pd.DataFrame({'key':['A','B','C']*2, 'data1':range(6), 'data2':rng.randint(0,10,6)}, columns = ['key', 'data1', 'data2'])
df
df.groupby('key').sum()
df.groupby('key').aggregate(['min','max','median'])

grouped = df.groupby('key')
grouped.aggregate({'data1':'min', 'data2':'max'})
grouped.aggregate({'data1':'min', 'data2':['max','min']})
#Filter: Select column
df.filter(items = ['key','data1'])
df.filter(like = '2', axis =0)
df.filter(like = 'd', axis = 1)
df.groupby('key').std()

#lambda
df['data2'].mean()
# listing those rows whose mean vaue of group is more than 4, first it is group by key and then find the mean and then list the rows
grouped.filter(lambda x:x['data2'].mean()>4)
grouped.filter(lambda x:x['data2'].std()>4)
grouped.transform(lambda x:x - x.mean())
x = 2
y = 3
product = lambda x,y:x*y
product(x,y)
grouped.apply(lambda x:x['data2']*2)

#Provide Group keys
df.groupby('key').sum()
df.groupby(df['key']).sum()

#change the index to key values
df2 = df.set_index('key')
df2
newmap = {'A':'Post Graduate','B':'Master of Science','C':'Bachelor of Science'}
df2.groupby(newmap).sum()
df2.groupby(str.lower).mean()
df2.groupby([str,str.lower,newmap]).mean()

#stack
df.groupby('key').sum().unstack()

# read or upload a csv file
students =pd.read_csv('D:\Shruti\PythonWork\PProject\Shruti_Spyder\Spyder\student2.csv')
students
students.drop(labels = 'Unnamed: 0', axis = 1, inplace=True)# how to drop a column
# other simple command to remove a column
del students['Unnamed:0']
students.head()
students.dtypes
students.select_dtypes(['object']) # only string
students.describe() # only numeric columns
classes = ['c1','c2','c3']
sclass = random.choice(classes,11)
sclass
students['class'] = pd.Series(sclass)
students.groupby('course')['class'].describe()
students.groupby('class').aggregate(['min', np.median, max])
students[['class', 'python', 'sas']].groupby('class').aggregate(['min', 'median', 'std', 'max'])

students[['course', 'hadoop', 'sas']].groupby('course').aggregate(['mean', 'median', 'std', 'max'])
pd.pivot_table(students, values = ['sas','hadoop'], index = 'course', aggfunc = [np.mean, np.median, min, max])

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
pd.pivot_table(students, index = 'gender', columns = 'class', values = 'sas').plot(kind = 'bar')
students
aggregation1 = {'sas':{'totalsas':'sum', 'avgsas': 'mean'}, 'hadoop': {'meanhadoop':'mean','stdhadoop': 'std'}}
aggregation2 = {'sas': 'mean'}
students[students['class']=='c3'].groupby('gender').agg(aggregation1)
