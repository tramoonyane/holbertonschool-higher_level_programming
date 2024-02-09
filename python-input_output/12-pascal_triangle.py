#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    - n (int): Number of rows to generate.

    Returns:
    - List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Each inner element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
