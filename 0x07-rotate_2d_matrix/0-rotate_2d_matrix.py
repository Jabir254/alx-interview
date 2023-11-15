#!/usr/bin/python3

"""0x07-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """rotate a 2d matrix
    returns nothing
    """

    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + 1]
            matrix[top][left + 1] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]

            matrix[bottom][right - i] = matrix[top + i][right]

            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
