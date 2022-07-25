"""
You are given an integer array coins representing coins of different denominations and an integer amount representing
a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class CoinChangeCombinations:
    @staticmethod
    def get_combinations(denominations: List[int], target_amount: int):
        dp = [0] * (target_amount + 1)
        dp[0] = 1
        for coin in denominations:
            for amount in range(target_amount + 1):
                if coin <= amount:
                    dp[amount] = dp[amount] + dp[amount - coin]

        return dp[target_amount]
