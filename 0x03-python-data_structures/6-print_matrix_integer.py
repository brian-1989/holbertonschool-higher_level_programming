#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # travel the elements of the matrix
    for i in range(0, len(matrix)):
        # condicition to when the matrix is empty
        if matrix == [[]]:
            print(end="\n")
            break
        # travel the positions that have each element
        for j in range(0, len(matrix[i])):
            # condicition to remove the space at final of each element
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d} ".format(matrix[i][j]), end="")
        print(end="\n")
