import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = x ** 3 - x ** 2 - 1
### has exactly one zero in [1,2]

a = 1
b = 2

fp = sy.diff(f,x)

g = (x ** 2 + 1) ** (1/3)

i = 0
def FixedPointMethod(x1):
    global i
    x2 = g.subs(x,x1)

    if abs(x1 - x2) > e:
        x1 = x2
        i+=1
        FixedPointMethod(x1)
    else:
        print('Solution m: ' +str(x2)+', iteration: '+str(i))

FixedPointMethod(random.randint(a,b+1))