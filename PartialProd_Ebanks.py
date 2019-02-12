# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:39:31 2019

@author: robbi
"""

import numpy as np
n=10000
x = np.zeros((0))
for ii in range(1,n):
    v= ((ii**3)-1)/((ii**3)+1)
    x=np.append(x,v)
print('This is the first sum. The first fifteen terms are', x[0:15])
print('The last fifteen terms are',x[9985:10000])

#Totally didnt copy paste the whole thing
n=10000
x = np.zeros((0))
for ii in range(1,n):
    v=np.exp(ii/100)/ii**10
    x=np.append(x,v)
print('This is the second sum. The first fifteen terms are', x[0:15])
print('The last fifteen terms are',x[9985:10000])

n=10000
x = np.zeros((0))
for ii in range(1,n):
    v=(ii**2)/2*ii
    x=np.append(x,v)
print('This is the third sum((i^5)/2i). The first fifteen terms are', x[0:15])
print('The last fifteen terms are',x[9985:10000])
#I think i did the partial product right