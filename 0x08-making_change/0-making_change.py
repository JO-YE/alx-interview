#!/usr/bin/python3
''' A fxn that determine the fewest number of coins needed to meet
   a given amount `total`'''


def makeChange(coins, total):
    '''Return: fewest number of coins needed to meet `total`
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1

        coins: is a list of the value of the coins in your possession
    '''
    # if the total amount i s0 or less, we need 0 coins
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed
    # for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make an amount of 0

    # Iterate through each coin value
    for coin in coins:
        # For each coin, we update the dp array to find the
        # minimum number of coins for each amount
        for i in range(coin, total + 1):
            # Update dp[i] only if using the current coin reduces
            # the number of coins needed
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot
    # be achieved using the given coins
    if dp[total] == float('inf'):
        return -1

    # The value at dp[total] gives us the minimum number of coins
    # needed to make the total amount
    return dp[total]
