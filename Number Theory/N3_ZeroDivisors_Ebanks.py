# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:10:35 2019

@author: robbi
"""

m=6
l=[]
n=[]
for i in range(1,m):
    for q in range(1,m):
        if (i*q)%m == 0:
            l.append(i)
for i in l:
    if i not in n:
        n.append(i)
print('Here are the zero divisors',n)
print('Here is the number of Zero Divisors:',len(n))
print('By the way your example is wrong 7=0 in Z7 so you cannot use it')