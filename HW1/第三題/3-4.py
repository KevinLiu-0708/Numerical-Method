import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = x ** 2- sy.sin(x) + sy.exp(2 * x) - 20
### has exactly one zero in [-5,-4],[1,2]

a = -5
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
        i+=1
        print('Solution m: ' + str(x2) +',error: '+str(abs(x1-x2))+', iteration: '+str(i))
        i=0


SecantMethod(0,1)
SecantMethod(-5,-4)
