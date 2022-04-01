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

i=0
def SecantMethod(x1,x2):
    global i

    x3 = float(-(x2 * f.subs(x,x1) - x1 * f.subs(x,x2)) / (f.subs(x,x2) - f.subs(x,x1)))

    x1 = x2
    x2 = x3

    if abs(x1 - x2) > e:
        i = i+1
        SecantMethod(x1,x2)
    else:
        print('Solution m: ' + str(x2) +', error: '+str(abs(x1-x2))+', iteration: '+str(i))
        i=0

SecantMethod(random.randint(a,b+1),random.randint(a,b+1))
