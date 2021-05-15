# Henry Song  |  MA375  |  Spring 2021
# Project #3B: Topic 7 - Solving Systems of Linear Equations
# File: GaussianElimination .py
# Dependencies: numpy, scipy
# Description: Uses Gaussian elimination to solve a system of linear 
#              equations (in matrix form). Solves for x when Ax = b.
#==========================================================================

import numpy as np
import scipy as sp

def create_augmented_matrix(a, b):
    a, b = a.tolist(), b.tolist()
    for x in range(len(a)): a[x].append(b[x])
    return a


def gauss(a, b):

    n = len(a)
    for i in range(0, n):
        a_m = abs(a[i, i])
        p = i

        for j in range(i+1, n):
            if abs(a[j][i]) > a_m:
                a_m = abs(a[j][i])
                p = j

        if p > i:
            for k in range(i, n):
                hold_value = a[i][k]
                a[i][k] = a[p][k]
                a[p][k] = hold_value
            hold_value = b[i]
            b[i] = b[p]
            b[p] = hold_value
        
        for j in range(i+1, n):
            m = a[j][i]/a[i][i]
            for k in range(i+1, n):
                a[j][k] = a[j][k] - m*a[i][k]
            b[j] = b[j] - m*b[i]
    
    x = b
    x[n- 1] = b[n-1]/a[n-1][n-1]

    #for i in reversed(range(n-1)):
    for i in range(n-1, 0):
        sum = 0
        for j in range(i+1, n):
            sum += a[i][j]*x[j]
        x[i] = (b[i] - sum)/a[i][i]
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

print(gauss(b_a, b_b))