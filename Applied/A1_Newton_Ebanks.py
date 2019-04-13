# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 20:03:21 2019

@author: robbi
"""

import numpy as np

N=100

TOL=1e-4
z0=1
l=[0]
n=1
f=lambda n: np.tan(n)-n-2
fp=lambda n: 1/(np.cos(n))**2-1

while np.abs(l[-1]-z0)>TOL and n<N:
    l.append(z0)    
    z0=z0-(f(z0)/fp(z0))
    n+=1
    if n == N:
        print('Hey! Itteration stopped')
if np.abs(l[-1]-z0)<TOL:
    print('Tolerance was hit')
for i in range(0,len(l)):
    print(l[i],'the difference from last',l[i]-(l[i-1]))