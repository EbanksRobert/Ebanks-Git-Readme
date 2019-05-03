# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:26:47 2019

@author: robbi
"""
import itertools
n=3

def d(l): 
    for i in range(0, len(p)-1):  
        yield l[i:i + n] 
def c(l): 
    for i in range(0, len(p)):  
        yield l[i:i + n+1]          
h=[]
l = list(map(list, itertools.product([0, 1], repeat=2**n)))
p = list(map(list, itertools.product([0, 1], repeat=n)))  
for i in l:
    if i[0:n] ==[0]*n and i[n]==1 and i[-1]==1 and [1]*n in list(d(i)) and [1]*(n+1) not in list(c(i)) :
        h.append(i)

print('Hey here is the # of solutions:',len(h),'Here are the solutions',h)
