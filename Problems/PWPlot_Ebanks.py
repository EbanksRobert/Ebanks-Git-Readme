# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:01:57 2019

@author: robbi
"""
#import matplotlib.pyplot as plt
import numpy as np
import decimal as dc
a=[]
def hrange(x,y,z):
    while x<y:
        yield x
        x+=z
for i in hrange (-3,-2,dc.Decimal('.1')):
    print (i)
    l=-3*((i+2)**2)+1
    a.append(l)
#print (a)
#x=np.arange(-3,-1.99,.01)
#y=0
#def func(f):
    #if f<-2==True:    
        #l=-3*((f+2)**2)+1
        #print (l)
#func(x)