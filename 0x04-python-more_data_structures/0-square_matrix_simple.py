#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col * col)
        new_matrix.append(new_row)
    return (new_matrix)
