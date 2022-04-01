import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = x ** 3 - sy.sin(x) - 1.15
### has exactly one zero in [1,2]

a = 1
b = 2

fp = sy.diff(f,x)

i=0
def NewtonMethod(t0):
    global i

    delta = float(-f.subs(x,t0) / fp.subs(x,t0))
    t1 = float(t0+delta)

    if abs(delta) > e:
        i = i+1
        NewtonMethod(t1)
    else:
        print('Solution m: ' +str(t1)+', error: '+str(abs(delta))+', iteration: '+str(i))

NewtonMethod(random.randint(a,b+1))