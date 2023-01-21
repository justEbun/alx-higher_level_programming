#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for each in matrix:
        for num in each:
            print("{:d} ".format(num))
        print("")
