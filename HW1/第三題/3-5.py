import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = sy.cos(x ** 2) - x ** 5 + 8.5 * sy.exp(2 * x) -3
### has exactly one zero in [-2,-1],[-1,0]

a = -2
b = 0

g1 = (sy.cos(x ** 2)+ 8.5 * sy.exp(2 * x) -3) ** 0.2
g2 = sy.ln(20+sy.sin(x)-x**2)/2

i = 0
def FixedPointMethod(x1):
    global i
    x2 = float(g2.subs(x,x1))

    if abs(x1 - x2) > e:
        x1 = x2
        i+=1
        FixedPointMethod(x1)
    else:
        i+=1
        print('Solution m: ' +str(x2)+' ,error:' +str(abs(x1-x2))+', iteration: '+str(i))

FixedPointMethod(-4)