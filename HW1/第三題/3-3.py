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
#arr=[]

def NewtonMethod(t0):
    global i
    #global arr

    delta = float(-f.subs(x,t0) / fp.subs(x,t0))
    t1 = float(t0+delta)

    if abs(delta) > e:
        i = i+1
        NewtonMethod(t1)
    else:
        i+=1
        print('Solution m: ' +str(t1)+', error: '+str(abs(delta))+', iteration: '+str(i))

        '''
        if not arr:
            arr.append(t1)
        else:
            for k in range(len(arr)):
                if round(t1,5) != round(arr[k],5):
                    arr.append(t1)
        '''
        i = 0

NewtonMethod(1)
NewtonMethod(-4)

