# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:39:12 2019

@author: robbi
"""

F0=1
F1=2
n=10000
x=0
m=5
fs=[]
e=[]

for i in range(1,n+1):
    
    #print
    x=F1+F0
    F0=F1
    F1=x
    fs.append(x)
    if x % m == 0:
        e.append(x)    
print ('Hey here is the percentage!',len(e)/len(fs))
print ('Here is the actual # of terms that are multiples:',len(e))
print (1/(m+1))