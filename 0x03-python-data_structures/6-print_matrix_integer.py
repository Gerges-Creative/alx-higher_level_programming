#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        i = 0
        for idx in matrix[row]:
            print("{:d}".format(idx), end='')
            row_len = len(matrix[row])
            if i < row_len - 1:
                print(" ", end='')
            i += 1
        print()
