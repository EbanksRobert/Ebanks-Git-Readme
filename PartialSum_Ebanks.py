# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 00:13:34 2019

@author: robbi
"""

import numpy as np
n=100
x = np.zeros((0))
for ii in range(1,n):
    v=np.log(ii**4+ii+3)/(np.sqrt(ii)+3)
    x=np.append(x,v)
print('This is the first sequence. The first fifteen terms are', x[0:15])
print('The last fifteen terms are',x[85:100])
#literally found the "x[0:15]" thingy by accident online https://stackoverflow.com/questions/4257394/slicing-of-a-numpy-2d-array-or-how-do-i-extract-an-mxm-submatrix-from-an-nxn-ar
n=100
x = np.zeros((0))
for ii in range(1,n):
    v=(2.718**(ii/100))/ii**10
    x=np.append(x,v)
print('This is the second sequence. The first fifteen terms are', x[0:15])
print('The last fifteen terms are',x[85:100])
n=100
x = np.zeros((0))
for ii in range(1,n):
    v=(ii**2)/2*ii
    x=np.append(x,v)
print('This is the third sequence((i^5)/2i). The first fifteen terms are', x[0:15])
print('The last fifteen terms are',x[85:100])
