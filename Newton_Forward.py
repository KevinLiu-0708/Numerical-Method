# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 09:34:20 2022

@author: Kirk Liu
"""
from sympy.abc import x
from math import floor, factorial

f = x ** 3 - 2 * x + 3

delta_arr = list()

x_arr = [-2, -1, 0, 1, 2, 3]
y_arr = [int(f.subs(x, t)) for t in x_arr]
delta_arr.append(y_arr)

for i in range(len(y_arr)-1):
    d_arr = list()
    for j in range(len(delta_arr[i])-1):
        former_arr = delta_arr[i]
        d_arr.append(former_arr[j+1] - former_arr[j])
    delta_arr.append(d_arr)
    
num = float(input('x: '))

s = (num - floor(num)) / abs(x_arr[0] - x_arr[1])

pos = x_arr.index(floor(num))

count = 0
result = 0
tmp = s
while len(delta_arr[count]) > pos:
    arr = delta_arr[count]
    if count == 0:
        result += arr[pos]
    elif count == 1:
        result += (arr[pos]*s)
    else:
        for k in range(1, count):
            tmp = tmp * (s-k)
        result += (tmp * arr[pos]/factorial(count))
    count+=1
    tmp = s

print('f(' + str(num) + ') = ' + str(result))