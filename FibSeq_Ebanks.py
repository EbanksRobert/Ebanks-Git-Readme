# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 18:17:28 2019

@author: robbi
"""

F0=1
F1=2
n=10
x=0
e=[]

for i in range(1,n+1):
    
    #print
    x=F1+F0
    print((x**2)-F0*(2*x+F1)==((-1)**(i-1)))
    F0=F1
    F1=x
    e.append(x)
    #print('x',x)
    #print('F0',F0)
    #print('F1',F1)
#print(e)
print ('Hey here are the last ten terms!',e[-10:])