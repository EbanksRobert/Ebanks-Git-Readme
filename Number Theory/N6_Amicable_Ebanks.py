# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:24:04 2019

@author: robbi
"""
N=1000
m=[]
n=[]
def f(x):    
    l=[]
    for i in range(1,x):
        if x/i == int(x/i):
            l.append(i)
    return(l)
for q in range(1,N):
    h=sum(f(q))
    if sum(f(h))==q:
        m.append(q)
        m.append(h)
for i in m:
    if i not in n:
        n.append(i)
print (n)