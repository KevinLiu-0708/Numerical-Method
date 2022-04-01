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

def BisectionMethod(r, t):
    global i

    fr = f.subs(x, r)
    ft = f.subs(x, t)
    try:
        if fr * ft < 0:

            m = (r + t) / 2
            fm = f.subs(x, m)

            if fr * fm < 0:
                t = m
            else:
                r = m

            if abs(r - t) > e:
                i = i + 1
                #print(r,t,abs(r-t),i)
                BisectionMethod(r, t)
            else:
                i+=1
                #print(r,t,abs(r-t),i)
                print('Solution m: ' + str(m) + ', error: ' + str(abs(r - t)) + ', iteration: ' + str(i))
                i = 0
        else:
            raise

    except:
        pass

for j in range(a,b+1):
    BisectionMethod(j, j+1)
