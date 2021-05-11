# Henry Song  |  MA375  |  Spring 2021
# Project #3B: Topic 7 - Solving Systems of Linear Equations
# File: GaussianElimination .py
# Dependencies: numpy, scipy
# Description: Uses Gaussian elimination to solve a system of linear 
#              equations (in matrix form). Solves for x when Ax = b.
#==========================================================================

import numpy as np
import scipy as sp


a_a = np.array([[14, 14, -9, 3, -5],
                [14, 52, -15, 2, -32],
                [-9, -15, 36, -5, 16],
                [3, 2, -5, 47, 49],
                [-5, -32, 16, 49, 79]])
a_b = np.array([[-15], 
                [-100], 
                [106], 
                [329], 
                [463]])
b_a = np.array([[9, 3, 2, 0, 7], 
                [7, 6, 9, 6, 4], 
                [2, 7, 7, 8, 2], 
                [0, 9, 7, 2, 2], 
                [7, 3, 6, 4, 3]])
b_b = np.array([[35], 
                [58], 
                [53], 
                [37], 
                [39]])

print(a_a)
print(a_b)