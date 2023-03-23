#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle up to n rows.

    :param n: the number of rows to generate
    :type n: int
    :return: a list of lists representing Pascal's Triangle up to n rows
    :rtype: list[list[int]]
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each subsequent row and add it to the triangle
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            val = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(val)
        row.append(1)
        triangle.append(row)

    # Format the triangle as a string with each row on a separate line
    triangle_str = ""
    for row in triangle:
        row_str = " ".join([str(val) for val in row])
        triangle_str += f"{row_str.center(n*2-1)}\n"

    # Convert the formatted string back to a list of lists of integers
    formatted_triangle = []
    for row in triangle_str.strip().split("\n"):
        formatted_row = [int(val) for val in row.split()]
        formatted_triangle.append(formatted_row)

    return formatted_triangle
