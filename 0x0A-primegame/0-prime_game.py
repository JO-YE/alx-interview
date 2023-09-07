#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''
    Prototype: def isWinner(x, nums)
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    '''
    def is_prime(n):
        '''Function to check if a number is prime'''
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def count_primes(n):
        '''Function to count prime numbers in a range'''
        count = 0
        for i in range(2, n + 1):
            if is_prime(i):
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    # Iterate through each round
    for n in nums:
        prime_count = count_primes(n)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
