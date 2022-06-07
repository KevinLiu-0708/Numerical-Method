# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:07:20 2022

@author: Kevin Liu
"""

import numpy as np
import pandas as pd
import math
from sympy import *

n = 100

def f(x):
    return (exp(-(x ** 2)/2) / sqrt(2 * pi)).evalf()

col_arr = np.around(np.arange(0, 0.01, 0.001), decimals=3)
row_arr = np.around(np.arange(0, 4, 0.01), decimals=2)

result=0

table = np.zeros((len(row_arr),len(col_arr)))
data=pd.DataFrame(table, index=row_arr, columns=col_arr)

for row in row_arr:
    for col in col_arr:
        if row == col and row == 0.0:
            data[col][row] = 0.5
            continue
        else:
            upper = row + col
            delta = (upper - 0) / n
            result = 0
            
            x_arr = np.linspace(0, upper, n+1)
            
            for k in range(len(x_arr)):
                if k == 0 or k == len(x_arr)-1:
                    result = result + f(x_arr[k])
                elif k % 2 != 0:
                    result = result + 4 * f(x_arr[k])
                else:
                    result = result + 2 * f(x_arr[k])
                    
        data[col][row] = round(0.5 + delta / 3 * result, 6)

data.to_excel('results.xlsx')