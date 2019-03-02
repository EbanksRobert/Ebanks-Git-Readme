# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 20:29:56 2019

@author: robbi
"""
#If you want ALL the triples before the "special" one change the 250's to ones and be ready to wait
import numpy as np
x= np.zeros((0,3))
e= np.zeros((0,4))
for i in range(250,500):
    
    for j in range(250,500):
       
        for k in range(250,500):
            if (i**2)+(j**2)==(k**2):
                h=[i,j,k,i+j+k]
                e=np.vstack([e,h])
                if (i+j+k==1026) and (i<j<k)==True:
                    v=[i,j,k]
                    x=np.vstack([x,v])
                    break
print('Hey here are all the prior triples',e)                    
print('Hey here is the special triple',x)
