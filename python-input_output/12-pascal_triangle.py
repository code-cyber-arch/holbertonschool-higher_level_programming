#!/usr/bin/python3
""" Function for pascal triangle"""


def pascal_triangle(n):
    """Create a function to return pascal triangle.

    Args:
        n: number of rows.

    Returns:
        Pascal riangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for i in range(1, i):
            row.append(prev_row[i - 1] + prev_row[i])

        row.append(1)
        triangle.append(row)

    return triangle
