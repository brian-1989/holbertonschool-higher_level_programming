#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    _len = len(matrix)
    for i in range(0, _len):
        if _len == 1:
            print(end="\n")
            break
        for j in range(0, _len):
            if j == _len -1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d} ".format(matrix[i][j]), end="")
        print(end="\n")
