# Henry Song  |  MA375  |  Spring 2021
# Project #3B: Topic 7 - Solving Systems of Linear Equations
# File: GaussianElimination.py
# Dependencies: numpy
# Description: Uses Gaussian elimination to solve a system of linear 
#              equations (in matrix form). Solves for x given A & B in 
#              Ax = B.
#==========================================================================

import numpy as np

# converts numpy array to python list(easier to work with) 
def create_augmented_matrix(a, b):
    a, b = a.tolist(), b.tolist()
    for x in range(len(a)): a[x].append(b[x])
    return a

# based off pseudocode from Epperson[1]
# comments also adapted from Epperson[1]
# modified to use augmented matrix instead of spearate A & B matrices
def gauss(a, b):
    aug_matrix = create_augmented_matrix(a,b)   #creates augmented matrix to use for elimination
    n = len(aug_matrix) #number of columns. Since gaussian elimination uses nxn matricies, this is also size of matrix
    
    #forward elimination
    for i in range(0, n):
        a_m = abs(aug_matrix[i][i]) # sets a_m to value on diagonal
        
        # searches for largest value of column i
        p = i   #counter for searching column i
        for j in range(i + 1, n):
            if abs(aug_matrix[j][i]) > a_m:
                a_m = abs(aug_matrix[j][i]) #replaces a_m with larger variable
                p = j   #set p as new index of larger value
        
        # swaps row i with row p
        for k in range(i, n+1):
            hold_value = aug_matrix[p][k]
            aug_matrix[p][k] = aug_matrix[i][k]
            aug_matrix[i][k] = hold_value
        
        # startt elimination for column i
        for j in range(i + 1, n):
            m = -aug_matrix[j][i]/aug_matrix[i][i]  # calculates multiplied to zero out entry
            for k in range(i, n+1):
                if i == j: aug_matrix[j][k] = 0
                else: aug_matrix[j][k] += m * aug_matrix[i][k]
    
    #backward substitution
    x = [0 for i in range(n)]   #blank matrix for x (solution) matrix
    for i in range(n-1, -1, -1):    # works backwards from last matrix row to first matrix row
        x[i] = (aug_matrix[i][n]/aug_matrix[i][i])  #solves x for row n-1
        for k in range(i-1, -1, -1): aug_matrix[k][n] -= aug_matrix[k][i] * x[i]

    return x

# prints nicer looking matrix (without the brackets)
def pretty_print_matrix(matrix, flag="column"):
    row = len(matrix)
    column = 0
    try:
        column = len(matrix[0])
        for i in range(row):
            print("|", end=" ")
            for j in range(column): 
                if j == (column-1): print(matrix[i][j], end=" ")
                else: print(matrix[i][j], end="\t")
            print("|")
    except TypeError:
        if flag == "column":
            for i in range(row):
                print("|", end=" ")
                print("%7.4f" % matrix[i], end=" ")
                print("|")
        elif flag == "row": 
            print("|", end=" ")
            for i in range(row): print("%7.4f" % matrix[i], end=" ")
            print("|")
    
# takes in user
def user_input():
    unknowns = int(input("Enter number of unknowns variables: "))
    print()

    # asks user for A matrix
    print("Enter 'A' matrix values:")
    print("Sample Input: 1 2 3 4")
    a = [[0] * unknowns] * unknowns
    for i in range(unknowns): a[i] = [float(j) for j in list((input("Enter row " + str(i+1) + ": ")).split(" "))]

    print()

    # asks user for B matrix
    print("Enter 'B' matrix values: ")
    print("Sample Input: 1 2 3 4")
    b = [float(j) for j in list((input("Enter row: ")).split(" "))]

    return np.array(a), np.array(b)

# generates a matrix of random integers between 0-1000 of a specified size.
def generate_matrix():
    size = int(input("Enter size of desired random matrix: "))
    a = np.random.randint(1000, size=(size, size))
    b = np.random.randint(1000, size=(size))
    return a, b

# hardcoded matrices from project 3B writeup
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

print("MA375 - Project #3B")
print("Henry Song")
print()

option = ""
# continues to loop unless user chooses to quit program
while option != "5":
    print("1. Use matrix equation A from Project 3B")
    print("2. Use matrix equation B from Project 3B")
    print("3. Use custom matrix equation")
    print("4. Use randomly generated matrix")
    print("5. Quits program")
    option = input("Please select an option: ")
    print()

    if option == "1":   # Performs gaussian elimation on given a_a and a_b matrices
        print("A = ")
        pretty_print_matrix(a_a)
        print()
        print("B = ")
        pretty_print_matrix(a_b, flag='column')
        print()
        print("Option 1: x = ", end=" ")
        pretty_print_matrix(gauss(a_a, a_b), flag='row')
        print()
    elif option == "2": #Performs gaussian elimination on given b_a and b_b matrices
        print("A = ")
        pretty_print_matrix(b_a)
        print()
        print("B = ")
        pretty_print_matrix(b_b, flag='column')
        print()
        print("Option 2: x = ", end=" ")
        pretty_print_matrix(gauss(b_a, b_b), flag='row')
        print()
    elif option == "3": #Performs gaussian elimination on user-provided a and b matrices
        a, b = user_input()
        print()
        print("A = ")
        pretty_print_matrix(a)
        print()
        print("B = ")
        pretty_print_matrix(b, flag='column')
        print()
        print("Option 3: x = ", end=" ")
        pretty_print_matrix(gauss(a, b), flag='row')
        print()
    elif option == "4": #Performs gaussian elimination on randomly generated a and b matrices
        a, b = generate_matrix()
        print()
        print("A = ")
        pretty_print_matrix(a)
        print()
        print("B = ")
        pretty_print_matrix(b, flag='column')
        print()
        print("Option 4: x = ", end=" ")
        pretty_print_matrix(gauss(a, b), flag='row')
        print()