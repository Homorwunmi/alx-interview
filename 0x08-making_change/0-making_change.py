#!/usr/bin/python3

"""
Module to fnd the minimum number of coins
required to make up a given atotal amount
"""


def makeChange(coins, total):
    """This function calculates the fewest number of coins to make change.

    Args:
        coins (list): list of available coin denominations to make change from
        total (int): given the total amount to make change for

    Returns:
        int: The fewest number of coins needed to make change
    """

    if total <= 0:
        return 0
    count = 0
    sorted_coins = sorted(coins, reverse=True)
    for coin in sorted_coins:
        while coin <= total and total > 0:
            count += 1
            total -= coin
    if total != 0:
        return -1
    else:
        return count
