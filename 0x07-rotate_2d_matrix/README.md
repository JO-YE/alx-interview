# 0x07. Rotate 2D Matrix

This project focuses on rotating a given n x n 2D matrix 90 degrees clockwise. The goal is to implement a Python function that performs the rotation in-place without returning a new matrix.

## Implementation Details

The rotation process involves two main steps:

- Transpose: Swap the elements at matrix[i][j] and matrix[j][i] for all valid pairs (i, j) within the matrix. This effectively transposes the matrix along its main diagonal.

- Reverse Rows: After transposing, reverse the elements in each row. This step completes the 90-degree clockwise rotation.
