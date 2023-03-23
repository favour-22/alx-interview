## Pascal's Triangle

This project contains tasks for working with Pascal's triangle.

## Tasks To Complete

+ [x] 0. **Pascal's Triangle**<br/>[0-pascal_triangle.py](0-pascal_triangle.py) contains a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`:
  
  + Returns an empty list if `n <= 0`.
  + You can assume `n` will be always an integer.
  
_The pascal_triangle function takes a single argument n which represents the number of rows to generate in Pascal's Triangle.
If the value of n is not an integer or if it is less than or equal to 0, an empty list is returned.
A list triangle is initialized to hold the rows of the Pascal's Triangle.
For each row i in the range 0 to n-1, a new list line is initialized to hold the values of that row.
For each value j in the range 0 to i, the corresponding value in the line list is computed according to the rule of Pascal's Triangle: the value at index j in row i is the sum of the values at index j-1 and j in row i-1.
If j is the first or last index in the row (i.e. j == 0 or j == i), the value at that index is set to 1.
Once the line list is complete, it is appended to the triangle list.
Finally, the triangle list is returned.
Overall, the code is well-organized, readable, and follows PEP 8 guidelines for Python code styling._

#Output
[1] 
[1 1] 
[1 2 1] 
[1 3 3 1] 
[1 4 6 4 1]


