# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:41:26 2022

@author: Kirk Liu
# 常理要求為 A 2x = 6b
# 課本為 A x = 3b
"""

import numpy as np
from numpy.linalg import inv
from sympy.abc import x
from math import factorial
from sympy import sympify

x_arr = [0, 0.2, 0.4, 0.6, 0.8, 1]
y_arr = [2, 2.008, 2.064, 2.216, 2.512, 3]
# = [0,4,6,7,13,15,19,24,26]
#y_arr = [0,3,8,12,7,5,2,3,5]

Coef_arr = np.zeros((len(x_arr), len(x_arr)))

Coef_arr[0][0] = 1
Coef_arr[len(x_arr)-1][len(x_arr)-1] = 1

for i in range(len(x_arr)):
    for j in range(len(x_arr)):
        if i == j:
            if i == 0 or i == len(x_arr) -1:
                continue
            else:
                Coef_arr[i][j] = 2 * ((x_arr[i] - x_arr[i-1]) + (x_arr[i+1] - x_arr[i]))
        else:
            if i == j + 1 and i != len(x_arr) - 1:
                Coef_arr[i][j] = (x_arr[i] - x_arr[i-1])
            if j == i + 1 and i >= 1:
                Coef_arr[i][j] = (x_arr[i+1] - x_arr[i])


b_arr = np.zeros(len(x_arr))

for i in range(len(x_arr)):
    if i == 0 or i == len(x_arr) - 1:
        b_arr[i] = 0
    else:
        tmp2 = 3*(y_arr[i+1] - y_arr[i]) / (x_arr[i+1] - x_arr[i])
        tmp1 = 3*(y_arr[i] - y_arr[i-1]) / (x_arr[i] - x_arr[i-1])
        b_arr[i] = tmp2-tmp1

c = np.dot(inv(Coef_arr), b_arr)

a = y_arr
b = np.zeros(len(x_arr)-1)
d = np.zeros(len(x_arr)-1)

for i in range(len(x_arr)-1):
    b[i] = (y_arr[i+1]-y_arr[i])/(x_arr[i+1]-x_arr[i]) - (x_arr[i+1]-x_arr[i]) * (2*c[i]+c[i+1]) / 3

for i in range(len(x_arr)-1):
    d[i] = (c[i+1] - c[i]) / (3 * (x_arr[i+1]-x_arr[i]))

func_list = list()

a = np.around(a,3)
b = np.around(b,3)
c = np.around(c,3)
d = np.around(d,3)

for i in range(len(x_arr)-1):
    print('S'+ str(i) +': ', end='')
    f = str(round(a[i],3))+ '+' \
        + str(round(b[i],3)) + '*(x-' +str(x_arr[i]) +') + ' \
        + str(round(c[i],3)) + '*(x-' +str(x_arr[i]) +')**2 + ' \
        + str(round(d[i],3)) + '*(x-' +str(x_arr[i]) +')**3'
    print(f)
    func_list.append(f)

print('================================================')


