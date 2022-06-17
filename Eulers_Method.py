import numpy as np
from sympy.abc import x,y

f = 2*x-y

y_arr = [-1]

n = 10
h = 1/n

x_arr = np.arange(0, 1.1, 0.1)

for i in range(len(x_arr)-1):
    yi = y_arr[i] + h * float(f.subs([(x, x_arr[i]), (y, y_arr[i])]))
    y_arr.append(round(yi, 6))
