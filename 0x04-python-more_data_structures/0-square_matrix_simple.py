#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(0, len(matrix)):
        # Within the condition, is the cycle for,
        # to iterate the positions of the elements and raise them squared
        new_matrix.append([j**2 for j in matrix[i]])
    return(new_matrix)
