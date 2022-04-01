import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')

f = x ** 2- sy.sin(x) + sy.exp(2 * x) - 20
### has exactly one zero in [-5,-4],[1,2]

a = -5
b = 2

i=0
def FalsePositionMethod(r,t):
    global i

    fr = f.subs(x,r)
    ft = f.subs(x,t)

    try:
        if fr * ft < 0:
            m = (r * ft - t * fr) / (ft - fr)
            m = float(m)

            fm = f.subs(x,m)

            if fr * fm < 0:
                mOld = t
                t = m
            else:
                mOld = r
                r = m

            if abs(m-mOld) > e:
                i = i+1
                FalsePositionMethod(r,t)
            else:
                i+=1
                print('Solution m: '+ str(m) + ', error: ' + str(abs(m-mOld)) + ', iteration: ' + str(i))
                i=0
        else:
            raise
    except:
        pass

for j in range(a,b+1):
    FalsePositionMethod(j,j+1)