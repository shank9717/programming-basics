"""
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class MinCoinChange:

    @staticmethod
    def get_min_coins(denominations: List[int], target_amount: int) -> int:
        dp = [float('inf')] * (target_amount + 1)
        dp[0] = 0
        for coin in denominations:
            for amount in range(target_amount + 1):
                if coin <= amount:
                    dp[amount] = min(dp[amount - coin] + 1, dp[amount])

        return -1 if dp[target_amount] == float('inf') else dp[target_amount]
