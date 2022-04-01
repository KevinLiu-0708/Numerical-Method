import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = sy.exp(x * 1.63 * sy.sin(x)) - 2.38 * x ** 2 - 3.6 * x + 1.24
### has exactly one zero in [-3,-2],[0,1],[2,3]

a = -3
b = 3

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
        i+=1
        print('Solution m: ' +str(t1)+', error: '+str(abs(delta))+', iteration: '+str(i))
        i=0

'''
for j in range(a-2,b+1):
    print(j/2)
    NewtonMethod(j/2)
'''
NewtonMethod(-2.5)
NewtonMethod(-1.5)
NewtonMethod(1)
NewtonMethod(1.5)