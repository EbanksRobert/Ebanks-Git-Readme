# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:18:32 2019

@author: robbi
"""

import numpy as np
N=10000
h=[]
v=[]
l=1
m=1
a = lambda n: n**2
b = lambda n: n**100
x = lambda n: n**20
for i in range(1,N):
    l*=1+(a(i)/b(i))
    h.append(l)
for i in range(1,N):
   m*=(1+x(.2))
   v.append(m)
print('Hey the first 15 terms of the first sequence are:',h[:15],' Now for the last 15:',h[-15:])
print('Hey the first 15 terms of the second sequence are:',v[:15],' Now for the last 15:',v[-15:])
