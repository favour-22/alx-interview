def pascal_triangle(n):
    """
    Returns a string representation of Pascal's Triangle up to n rows.

    :param n: the number of rows to generate
    :type n: int
    :return: a string representation of Pascal's Triangle up to n rows
    :rtype: str
    """
    if n <= 0:
        return ""

    triangle = [[1]]
    output = "1\n"
    for i in range(1, n):
        row = [1]
        output_row = "1"
        for j in range(1, i):
            val = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(val)
            output_row += " " + str(val)
        row.append(1)
        triangle.append(row)
        output_row += " 1\n"
        output += output_row

    return output
