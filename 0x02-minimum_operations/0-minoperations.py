#!/usr/bin/python3
"""Module for task 0
"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.

    In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste characters
    in the file.

    Args:
        n (int): The number of desired H characters.

    Returns:
        int: The number of minimal operations needed to get n H characters
    or 0 if it is impossible to achieve n.
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    counter = 0
    done = 1
    while done < n:
        if counter == 0:
            counter = done
            done +=counter
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
           counter = done
            done += counter
            ops_count += 2
        elif counter > 0:
            done += counter
            ops_count += 1
    return ops_count
