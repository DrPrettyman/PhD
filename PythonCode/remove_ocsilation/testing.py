#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from math import *

N = 100
d = 2
B = np.matrix([[1,2],[2,3]])
S = np.matrix([[1,0],[0,1]])

x0 = np.matrix([[0.1],[-0.1]])

X = np.zeros((N,d))

X[0,:] = np.transpose(x0)

print np.transpose(np.matrix(X[0,:]))
print X[0,:]


eta = np.random.randn(2,1)
print np.dot(B,x0)

