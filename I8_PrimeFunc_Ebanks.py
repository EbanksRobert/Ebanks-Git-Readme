# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:38:54 2019

@author: robbi
"""

n=100
m=2
v=[]
h=[]
p=1
def prime_check(x):
    l=[]
    for i in range(2,x):
        if x/i==int(x/i):
            l.append(x)
            break
    if v==l:
        return(True)
    else:   
        return(False)

while n>len(h):
    p=p+1
    if prime_check(p)==True:
        h.append(p)
print('Hey the',n,'prime is', h[-1:])
