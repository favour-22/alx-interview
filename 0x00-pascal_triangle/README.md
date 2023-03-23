## Pascal's Triangle

This project contains tasks for working with Pascal's triangle.

## Tasks To Complete

+ [x] 0. **Pascal's Triangle**<br/>[0-pascal_triangle.py](0-pascal_triangle.py) contains a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:
  + Returns an empty list if `n <= 0`.
  + You can assume `n` will be always an integer.
_This implementation starts by checking if n is less than or equal to 0. If it is, an empty list is returned._
_If n is greater than 0, the function initializes the triangle with the first row, which consists of a single element with the value 1._
Then, for each row from the second to the nth row, the function generates a new row by iterating over the previous row and calculating the value of each element based on the values of the two elements above it. The new row is then appended to the triangle.
Finally, the function returns the completed triangle.
