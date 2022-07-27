"""
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
For example, if the length of the rod is 8 and the values of different pieces are given as the following,
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
"""
from typing import List


class RodCutting:
    @staticmethod
    def max_price(prices: List[int]) -> int:
        rod_size = len(prices)
        max_prices = [0] * (rod_size + 1)
        for sub_size in range(1, rod_size + 1):
            max_val = -float('inf')
            for price in range(sub_size):
                max_val = max(max_val, prices[price] + max_prices[sub_size - price - 1])
            max_prices[sub_size] = max_val

        return max_prices[rod_size]
