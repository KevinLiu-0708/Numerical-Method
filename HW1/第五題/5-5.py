import random
import sympy as sy
import numpy as np
import math

e = 0.000001

x = sy.Symbol('x')
y = sy.Symbol('y')

# f x函數
# g y函數

## 第一式
f1 = 2+3*y-x*y
f2 = (2+3*y)/(y+1)
f3 = (2+3*y-x)/y

## 第二式
g4 = (7+2.5*y+5*x)/x
g5 = (7+5*x-x*y)/(-2.5)
g6 = (7+5*x)/(x-2.5)

i = 0
def FixedPointMethod(x1,y1):
    global i

    x1Old = x1
    y1Old = y1

    x1 = float(f2.subs([(x,x1Old),(y,y1Old)]))
    y1 = float(g6.subs([(x,x1),(y,y1Old)]))

    error = float(((x1-x1Old) ** 2 + (y1-y1Old) ** 2) ** (0.5) / ((x1 ** 2) + (y1 ** 2)) ** (0.5))

    print(x1,y1,error)

    if abs(error) > e:
        x1 = x1
        y1 = y1
        i+=1
        FixedPointMethod(x1,y1)
    else:
        i+=1
        print('Solution x: ' +str(x1)+', Solution y:'+str(y1)+', iteration: '+str(i))

FixedPointMethod(1, 2)
