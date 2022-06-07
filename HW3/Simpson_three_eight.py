# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:53:19 2022

@author: 111036
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:07:20 2022

@author: 111036
"""

import numpy as np
import pandas as pd
import math
from sympy import *

n = 15

def f(x):
    return (exp(-(x ** 2)/2) / sqrt(2 * pi)).evalf()
    #return sqrt(x)


col_arr = np.arange(0, 0.01, 0.001)
row_arr = np.arange(0, 4, 0.01)


tmp=0

table = np.zeros((len(row_arr),len(col_arr)))
data=pd.DataFrame(table)

for i in range(len(row_arr)):
    for j in range(len(col_arr)):
        if i == j and i == 0:
            data[j][i] = 0.5
            continue
        else:
            upper = row_arr[i] + col_arr[j]
            delta = (upper - 0) / n
            tmp = 0
            
            x_arr = np.linspace(0, upper, n+1)
            #print(upper)
            
            for k in range(len(x_arr)):
                if k == 0 or k == len(x_arr)-1:
                    #print(str(x_arr[k]) + '----- ' +'1*'+str(x_arr[k])+ '----- ' + str(f(x_arr[k])))
                    tmp = tmp + f(x_arr[k])
                elif k % 3 != 0:
                    #print(str(x_arr[k]) + '----- ' +'4*'+str(x_arr[k])+ '----- ' + str(4*f(x_arr[k])))
                    tmp = tmp + 3 * f(x_arr[k])
                else:
                    #print(str(x_arr[k]) + '----- ' +'2*'+str(x_arr[k])+ '----- ' + str(2*f(x_arr[k])))
                    tmp = tmp + 2 * f(x_arr[k])
                    
        data[j][i] = round(0.5 + (delta * 3 / 8) * tmp, 6)
        #print(data[j][i])
        #print()

#data = data.reindex(map(str, row_arr))
#data.columns = map(str, col_arr)