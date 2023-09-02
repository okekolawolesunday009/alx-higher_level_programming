#!/usr/bin/python3
"""function that prints the MATRIX DIVIDED BY DIV"""


def matrix_divide(matrix, div):
    """function that prints the MATRIX DIVIDED BY DIV
    Args:
        matrix: the matrix 
        div: the number to divided with
    Raises:
        TypeError: matrix must be a matrix of integers/floats
                   div must be a number 
                   matrix must be a matrix (list of lists) of integers/floats
        ValueError: size <= 0
        ZeroDivisionError: 
    """
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif div < 0:
        raise TypeError('div must be a number')
    elif not  isinstance(matrix, list):
        TypeError('matrix must be a matrix (list of lists) of integers/floats')
    elif not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError('matrix must be a matrix of integers/floats')
    result = []
    for i in range(len(matrix)):
        row_result = []
        for j in range(len(matrix)):
            row_result.append(matrix[i][j]/div)
            result.append(row_result) 
    print({}, result) 