#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for idx in matrix[row]:
            print("{:d}".format(idx), end='')
            if matrix[row][idx + 1] != None:
                print(" ", end='')

        print()
