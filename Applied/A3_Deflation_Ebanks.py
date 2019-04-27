# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:04:15 2019

@author: robbi
"""

import numpy as np
#Erase high degree terms that are now zero
# Assumed that highest degree of p is last element of list
def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1
            
        
    del p[highest_deg+1:]
    
    
    return p
g=[2,2,3]#Deg(g) must be larger than Deg(f) for some reason
f=[3,2]
r=[]
q=0
for i in f:
    r.append(i)
def i(f,g):#ATTENTION ATTENTION THIS DOES **NOT** WORK IF 1>len(g)/len(f)
    n=clean_poly(f)#LT(f)/LT(g)
    m=clean_poly(g)
    h= int(len(m)/len(n))
    l= m[-1]/n[-1]
    v=[0]*(len(n)+1)
    v[h]=l
    v=clean_poly(v)
    return v
def sub_list(x,y):#This does x[i]-y[i]=new_list[i]
    d=[]
    t=[]
    for a in x:
        d.append(a)
    for a in y:
        t.append(a)
    for i in range(0,len(x)):
        t[i]= d[i]-t[i]
    return t
def mult_list(x,y):#This does x[i]*y[i]=new_list[i]
    d=[]
    t=[]
    for a in x:
        d.append(a)
    for a in y:
        t.append(a)
    for i in range(0,len(x)):
        t[i]= t[i]*d[i]
    return t
while clean_poly(r)!=[0]*len(r)and r!=[] and sum(i(r,g))==int(sum(i(r,g))):
    q=q+sum(i(r,g))
    r= sub_list(r,mult_list(i(r,g),g))
print('This is f:',f,'g:',g,'q:',q,'r:',r)