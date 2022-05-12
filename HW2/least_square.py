# -*- coding: utf-8 -*-
"""
Created on Thu May 12 13:21:44 2022

@author: 111036
"""

from sympy import *
from sympy.plotting import plot
import random
import numpy as np
from numpy.linalg import inv

x = symbols('x')

expr = x ** 2 - x + 3
#expr = sin(x)


'''
x_arr = [0, 0.5, 1.0, 1.5, 2.0, 2.5]
y_arr = [0, 0.2, 0.27, 0.3, 0.32, 0.33]

'''
x_arr = []
y_arr = []

random_numbers = int(input('random_numbers: '))
for i in range(random_numbers):
    num = random.randint(-30, 30)
    x_arr.append(num)
    y_arr.append(float(expr.subs(x,num)))

n = int(input('n: '))


left_arr = np.zeros((n,n))
ans_arr = np.zeros((n,1))

# 左矩陣
for j in range (0,n):
    for k in range(0,n):
        if j == 0 and k == 0:
            left_arr[j][k] = len(x_arr)
        else:
            print(j,k)
            tmp = [number ** (j+k) for number in x_arr]
            left_arr[j][k] = sum(tmp)
    
# 右矩陣
for j in range(n):
    if j == 0:
        ans_arr[j][0] = sum(y_arr)
    else:
        tmp = [number ** j for number in x_arr]
        ans_arr[j][0] = sum(np.array(tmp) * np.array(y_arr))

# 反矩陣
inverse = inv(left_arr)
result = np.dot(inverse, ans_arr)

# 近似equation
final_eq = 0
for i in range(n):
    tmp2 = result[i][0] * (x ** i)
    final_eq = final_eq + tmp2

print('Final Equation: ', final_eq)
# error
final_y_arr = []
error_arr = np.zeros((random_numbers,1))
for h in range(len(x_arr)):
    error_arr[h][0] = abs(float(final_eq.subs(x,x_arr[h])) - y_arr[h])


error = [number ** 2 for number in error_arr]
error = sum(error)
print('error: ', error)
 
# plot
p1 = plot(final_eq)
p2 = plot(expr)
p1.append(p2[0])
p1.show()
