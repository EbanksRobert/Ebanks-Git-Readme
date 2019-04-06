# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:13:58 2019

@author: robbi
"""
import numpy as np

P=200
o= np.array([['p','# of Residuals']])
z= np.array([['p','-1 is a residue']])
def Res(x):#turned this into a def function because i already had it written out before I tried to use arrays
    h=[]
    l=[]
    m=x
    for i in range(0,m):    
        for ii in range(0,m**2):    
            if (ii**2)%m == i:
                l.append(i)
    for v in l:
        if v not in h:
            h.append(v)
    return(len(h))
def Neg(m):#The numpy array stores Truth and False values as 1 and 0 respectivly 
    for i in range(0,m):    
        if (i**2)%m == -1%m:
            return(True)
    return(False)
def prime_check(x):
    v=[]
    l=[]
    for i in range(2,x):
        if x/i==int(x/i):
            l.append(x)
            break
    if v==l:
        return(True)
    else:
        return(False)
for k in range(2,P+1):  
    if prime_check(k)==True:
        q=np.array([[k, Res(k)]])
        o=np.vstack((o,q))
for k in range(2,P+1):
    if prime_check(k)==True:
        e=np.array([[k,Neg(k)]])
        z=np.vstack((z,e))

print('Here is the count per modulus',o)
print('Here is the check if -1 is a residue (Note: 1=True 0=False',z)