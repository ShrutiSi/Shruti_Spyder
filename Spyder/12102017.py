# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:02:14 2017

@author: saach
"""
# File input and output, eval to be used only for formula or mathematical expression
str = eval(input("Enter your input: "))
print("Recieved inout is: ",str)
str = input("Enter your input: ")
print("Recieved inout is: ",str)

for i in range(0,5):
    print(i)
    
#to know the current qorking directory
import os
os.getcwd()
os.listdir('D:\\')
os.mkdir("D:\\test")
os.chdir("D:\\test")
os.getcwd()
os.chdir("..")
os.getcwd()
os.chdir( 'D:\\Shruti\\PythonWork\\PProject\\Shruti_Spyder\\Spyder')
os.getcwd()
#File Open
#file object = open(file_name,[,access_model,buffering])
f=open("abc.text",'r')
f = open( 'D:\\Shruti\\PythonWork\\PProject\\Shruti_Spyder\\Spyder\\abc.txt')
print(f.name)
print(f.mode)# know the mode whether read or write mode
f.close()
os.rename("abc.txt", "xyz.txt") # rename a file after closing it
os.remove("xyz.txt") #remove a file
#Create a new file and write sometext in it by using below command
f= open("foo.txt", "w")
f.write("Python is a great language.\r\n Yeah its great!!\r\n")
f.close()
f= open("foo.txt","r+")
str = f.read(20);
print('Read string is: ', str)
f.tell() # tells u the cursor position
f.seek(0,0) # move the cursor back to the starting
f.seek(6,0)
f.close()
fo = open('sunday.txt', 'w')
fo.close()
fo.write("Today is first sunday\n")
fo.write('first Sunday\n')
fo.write('Today is Sunday\n')
fo.write('Sunday\n')
# to print the length of the longest line and print the same
def input_stats(filename):
    input = open(filename)
    longest = ""
    for line in input:
        if len(line) > len(longest):
            longest = line
            print("longest line =", len(longest))
            print(longest)
input_stats("sunday.txt")
# to open all the lines in a fle
fo= open('sunday.txt','r+')
for line in fo:
    line=line.strip("\n")
    print(line)
fo.close()

name = 'Brave sir Robin'
word = name.split()
print(word)

s = "Jessica 31 647.28"
name, age, money = s.split()
print(name)
print(age)
print(money)

import os
Hours = open('hours.txt', 'w')
Hours.write('123 Suzy 9.5 8.1 7.6 3.1 3.2\n')
Hours.write('456 Brad 7.0 9.6 6.5 4.9 8.8\n')
Hours.write('789 Jenn 8.0 8.0 8.0 8.0 7.5\n')
Hours.close()
# to read the file, give following command
H = open('hours.txt', 'r')
for line in H:
    ID, Name, Monday, Tuesday, Wednesday, Thursday, Friday = line.split()
    Total = float(Monday)+float(Tuesday)\
            +float(Wednesday)+float(Thursday)+float(Friday)
    print(Name,"ID", ID, "worked",\
          round(Total,2),"hours:", round(Total/5), "/day")