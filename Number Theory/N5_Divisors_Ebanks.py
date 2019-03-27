# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:40:17 2019

@author: robbi
"""
def f(x):    
    l=[]
    for i in range(1,x):
        if x/i == int(x/i):
            l.append(i)
    return(l)
print(f(100))        