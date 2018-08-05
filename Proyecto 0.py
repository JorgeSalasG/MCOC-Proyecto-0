# -*- coding: utf-8 -*-
"""
Created on Sun Aug 05 09:05:06 2018

@author: Jorge
"""
import matplotlib.pylab as plt
import numpy as np

def y32(x):
    y=np.sqrt(((x**2)+1), dtype=np.float32)-x
    return y

def y64(x):
    y=np.sqrt(((x**2)+1), dtype=np.float64)-x
    return y
error_relativo=[]
n=[]
for i in range(1,100):
    n.append(i)

for x in range(1,100):
    error=(np.absolute(y32(x)-y64(x))/y64(x))*100.0
    error_relativo.append(error)
    
plt.figure()

plt.plot(n,error_relativo)

plt.show()
