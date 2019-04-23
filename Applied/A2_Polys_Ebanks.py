# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:34:41 2019

@author: robbi
"""

import numpy as np
#first term is smallest exponent
p=[1,1,1]
#evaluate point
def ev(x,y):
    v=np.zeros(len(x))
    for i in range(0,len(x)):
        v[i]=x[i]*y**i
    return ('The poly at the given point',y,' is',sum(v))
#derivative
def der(x):
    k=x
    k.append(0)
    v=np.zeros(len(x))
    for i in range(0,len(x)-1):
        v[i-1]=k[i]*(len(x)-(len(x)-i))
    return(v)
#integral
def inte(x,y,z):
    v=np.zeros(len(x)+1)
    k=np.zeros(len(x)+1)
    for i in range(1,len(x)+1):
        v[i]=x[i-1]
    for i in range (1,len(v)):
        v[i]= v[i]/(len(x)-(len(x)-i))
    for i in range(0,len(x)+1):
        k[i]=v[i]*z**i
        v[i]=v[i]*y**i
    return('The definite integral between',y,'and',z,'is', sum(k)-sum(v))
print(ev(p,2),inte(p,1,2),ev(der(p),2))