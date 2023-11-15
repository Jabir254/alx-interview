#!/usr/bin/python3

"""0x07-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """rotate a 2d matrix
    returns nothing
    """
    n = len(matrix)

    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        for i in range(first, last):
            top = matrix[first][i]
            # Move left element to top
            matrix[first][i] = matrix[last - (i - first)][first]

            # Move bottom element to left
            matrix[last - (i - first)
                   ][first] = matrix[last][last - (i - first)]

            # Move right element to bottom
            matrix[last][last - (i - first)] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top
