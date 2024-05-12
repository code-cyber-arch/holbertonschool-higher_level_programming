#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [None] * len(matrix)
    for i in range(len(matrix)):
        new_matrix[i] = [None] * len(matrix[i])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
