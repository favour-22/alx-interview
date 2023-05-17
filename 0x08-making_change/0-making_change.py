#!/usr/bin/python3

def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number of
    coins needed to meet a given amount total.

    :param coins: list of coin values
    :param total: amount to reach
    :return: fewest number of coins needed to reach total
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total+1)
    dp[0] = 0

    for c in coins:
        for i in range(c, total+1):
            dp[i] = min(dp[i], dp[i-c]+1)

    return dp[total] if dp[total] != float('inf') else -1
