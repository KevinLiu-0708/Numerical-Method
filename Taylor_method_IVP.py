import numpy as np
from sympy.abc import x,y
from sympy import diff, factorial, exp, sympify


# With y in equation
f = x+y

x0 = 0
y0 = 1
y_arr = [y0]

n = 3

for i in range(n):
    if i == 0:
        ans = float(f.subs(x,x0))
    else:
        ans = diff(f,x).subs(x,x0)
    yi = y_arr[i] + float(ans)
    y_arr.append(round(yi, 6))
    
func = str()

for i in range(len(y_arr)):
    if i == 0:
        func += (str(y_arr[i]) + ' + ')
    elif i == 1:
        func += ('x*' + str(y_arr[i]) + ' + ')
    elif i == len(y_arr) - 1:
        func += ('(x**' + str(i) + ')*' + str(y_arr[i]))
    else:
        func += ('(x**' + str(i) + ')*' + str(y_arr[i]) + ' + ')
        
print(func)
func = sympify(func)
ans = float(func.subs(x,1))
