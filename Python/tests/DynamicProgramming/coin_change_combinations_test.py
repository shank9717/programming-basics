import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.UnboundedKnapsack.coin_change_combinations import CoinChangeCombinations


class TestCoinChangeCombinations(TestCase):
    def setUp(self) -> None:
        self.coin_change = CoinChangeCombinations()

    def test_min_coin_change_1(self):
        amount = 5
        coins = [1, 2, 5]
        res = self.coin_change.get_combinations(coins, amount)
        self.assertEqual(4, res)

    def test_min_coin_change_2(self):
        amount = 11
        coins = [1, 2, 5]
        res = self.coin_change.get_combinations(coins, amount)
        self.assertEqual(11, res)

    def test_min_coin_change_3(self):
        amount = 3
        coins = [2]
        res = self.coin_change.get_combinations(coins, amount)
        self.assertEqual(0, res)

    def test_min_coin_change_4(self):
        amount = 10
        coins = [10]
        res = self.coin_change.get_combinations(coins, amount)
        self.assertEqual(1, res)


if __name__ == '__main__':
    unittest.main()
