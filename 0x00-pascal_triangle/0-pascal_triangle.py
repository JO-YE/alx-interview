#!/usr/bin/python3
''' Creating a function that returns list of lists of intergers.'''


def pascal_triangle(n):
    '''n represent the number of row to generate in pascal triangle'''
    if n <= 0:
        return []

    # represent row index 0 and column index 0. `column == row`
    # triangle is a list of lists
    triangle = [[1]]

    # looping from index 1
    for row in range(1, n):
        current_row = [1]

        # the code retrieves the row above the current row
        # in the first case, row rep `index 1` - 1 will give us row of index 0.
        previous_row = triangle[row - 1]

        for col in range(1, row):
            # to calculate the values for the current row
            current_row.append(previous_row[col - 1] + previous_row[col])
            # previous_row[col - 1] represents the element to the left
            # previous_row[col - 1] represents the element to the left

        current_row.append(1)  # to ensure every row ends with 1
        triangle.append(current_row)

    return triangle
