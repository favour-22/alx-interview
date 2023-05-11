#!/usr/bin/python3
"""
This module provides a function for rotating an n x n 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list]): A 2D matrix to rotate.

    Returns:
        None. The matrix is modified in-place.
    """
    n = len(matrix)
    # transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row of the transposed matrix in-place
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

