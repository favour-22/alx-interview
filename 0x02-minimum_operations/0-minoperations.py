#!/usr/bin/python3
"""
This module contains a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed to reach n H characters.

    Raises:
        ValueError: If n is less than or equal to 1.
        Exception: If it is impossible to reach n H characters using Copy All and Paste operations.
    """
    if n <= 1:
        raise ValueError("n must be greater than 1.")
    
    operations = 0
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    
    if n != 1:
        raise Exception("It is impossible to reach {} H characters using Copy All and Paste operations.".format(n))
    
    return operations


if __name__ == '__main__':
    n = 9
    print("minOperations({}) = {}".format(n, minOperations(n)))
