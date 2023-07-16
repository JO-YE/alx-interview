#!/usr/bin/python3
'''This method calculate the fewest number of operation needed to result
   in exactly `n` `H` characters in the file.
   '''

def minOperations(n):
    '''`n` represent the desired number of H characters in the file
        return an integar
        if `n` is impossible to achieve, return 0
    '''
    # If n is less than or equal to 1, no operations are needed
    if n <= 1:
        return 0
    # Starting with a large value to keep track of the minimum operations
    min_ops = float('inf')

    # Looping through all possible divisors of n
    for divisor in range(2, n + 1):
        # Checking if the current divisor divides `n` evenly
        if n % divisor == 0:
            # Calculate the number of operations needed for this divisor
            num_operations = divisor + minOperations(n // divisor)

            # Updating the minimum number of operations if the current
            # divisor requires fewer operations
            min_ops = min(min_ops, num_operations)

    # Return the minimum number of operations needed for n
    return min_ops
