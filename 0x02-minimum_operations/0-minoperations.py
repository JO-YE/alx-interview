#!/usr/bin/python3
'''This method calculate the fewest number of operation needed to result
   in exactly `n` `H` characters in the file.
   '''


def minOperations(n):
    '''`n` represent the desired number of H characters in the file
        return an integar
        if `n` is impossible to achieve, return 0
    '''
    if n <= 1:
        return 0

    num_operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            num_operations += divisor
        else:
            divisor += 1

    return num_operations
