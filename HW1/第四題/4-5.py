import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = sy.exp(x * 1.63 * sy.sin(x)) - 2.38 * x ** 2 - 3.6 * x + 1.24
### has exactly one zero in [-3,-2]:[-4,-3], [0,1]:[0,1], [1,2]:[1,2], [2,3]:[4,5]

a = -3
b = 3

g1 = (sy.exp(x * 1.63 * sy.sin(x)) - 2.38 * x ** 2 + 1.24)/3.6
g2 = ((sy.exp(x * 1.63 * sy.sin(x)) - 3.6 * x + 1.24)/2.38) ** 0.5

i = 0
def FixedPointMethod(x1):
    global i
    x2 = g2.subs(x,x1)

    if abs(x1 - x2) > e:
        x1 = x2
        i+=1
        FixedPointMethod(x1)
    else:
        print('Solution m: ' +str(x2)+', iteration: '+str(i))

FixedPointMethod(0)