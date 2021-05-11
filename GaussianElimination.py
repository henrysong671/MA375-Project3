# Henry Song  |  MA375  |  Spring 2021
# Project #3B: Topic 7 - Solving Systems of Linear Equations
# File: GaussianElimination .py
# Dependencies: numpy, scipy
# Description: Uses Gaussian elimination to solve a system of linear 
#              equations (in matrix form). Solves for x when Ax = b.
#==========================================================================

import numpy as np
import scipy as sp

def gauss(a, b):
    for i in range(len(a)-1):
        a_m = abs(a[i, i])
        p = i

        j = i + 1
        for j in range(len(a)):
            if abs(a[j,i]) > a_m:
                a_m = abs(a[j, i])
                p = j

        if p > i:
            k = i
            for k in range(len(a)):
                hold_value = a[i, k]
                a[i, k] = a[p, k]
                a[p, k] = hold_value
            hold_value = b[i]
            b[i] = b[p]
            b[p] = hold_value
        
        j = i + 1
        for j in range(len(a)):
            m = a[j,i]/a[i,i]
            k = i + 1
            for k in range(len(a)):
                a[j,k] = a[j,k] - m*a[i,k]
            b[j] = b[j] - m*b[i]
    
    x = np.zeros(len(b))
    x[len(a)-1] = b[len(a)-1]/a[len(a)-1, len(a)-1]

    for i in reversed(range(1)):
        sum = 0
        j = i + 1
        for j in range(len(a)):
            sum += a[i,j]*x[j]
        x[i] = (b[i] - sum)/a[i,i]
    return x



a_a = np.array([[14, 14, -9, 3, -5],
                [14, 52, -15, 2, -32],
                [-9, -15, 36, -5, 16],
                [3, 2, -5, 47, 49],
                [-5, -32, 16, 49, 79]])
a_b = np.array([-15, -100, 106, 329, 463])
b_a = np.array([[9, 3, 2, 0, 7], 
                [7, 6, 9, 6, 4], 
                [2, 7, 7, 8, 2], 
                [0, 9, 7, 2, 2], 
                [7, 3, 6, 4, 3]])
b_b = np.array([35, 58, 53, 37, 39])

print(gauss(a_a, a_b))