#!/usr/bin/python3
def matrix_divided(matrix, div):

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    row_len = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_type)
        if len(row) != row_len:
            raise TypeError(msg_size)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg_type)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2)for num in row]for row in matrix]
