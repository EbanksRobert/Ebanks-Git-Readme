# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:16:53 2019

@author: robbi
"""
import numpy as np
def p(x):
    l=[]
    v=[]
    for i in range(2,x):
        if x/i==int(x/i):
            l.append(x)
            break
    if v==l:
        return(True)
    else:   
        return(False)
def o(x):
    if x/2 == int(x/2):
        return False
    else:
        return True

for i in range (1,6000):
    Goldbach = False
    if p(i) == False and o(i) == True:
        for n in range(1,i):
            if Goldbach == True:
                break
            if p(n)==True:
                for q in range(1,int(np.sqrt(i))):
                    if i == n + 2*(q**2):
                        Goldbach = True
                        break
        if Goldbach==False:
            print('Hey doing this assignment made me wanna die. Oh and Goldbach fails because of',i)
            break