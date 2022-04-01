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
        print('Solution m: ' + str(x2) +', error: '+str(abs(x1-x2))+', iteration: '+str(i))
        i=0

'''
for j in range(a,b+1):
    x1 = random.randint(-4,4)
    x2 = random.randint(x1,10)
    print(x1,x1+1)
'''

SecantMethod(-4,-3)
SecantMethod(0,1)
SecantMethod(1,2)
SecantMethod(4,5)
