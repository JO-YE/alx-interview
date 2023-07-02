# 0x00. Pascal's Triangle
<p style="font-size:16px;">This repository contains an implementation of Pascal's Triangle in the Pascal programming language. Pascal's Triangle is a mathematical construct that consists of triangular numbers arranged in a triangular pattern. Each number in the triangle is the sum of the two numbers directly above it.</p>

- In Pascal triangle, each row has a number of elements equal to its row number plus 1.
	- a row of index 0 has one element, and index 1 will have 2 elements.
 
 #### ***In Pascal's Triangle, every row starts and ends with the value 1***

## Task
### [0-pascal_triangle](./0-pascal_triangle.py)
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

	- Returns an empty list if n <= 0
	- You can assume n will be always an integer
