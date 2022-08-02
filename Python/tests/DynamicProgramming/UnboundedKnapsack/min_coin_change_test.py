import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.UnboundedKnapsack.min_coin_change import MinCoinChange


class TestMinCoinChange(TestCase):
    def setUp(self) -> None:
        self.coin_change = MinCoinChange()

    def test_min_coin_change_1(self):
        amount = 5
        coins = [1, 2, 5]
        res = self.coin_change.get_min_coins(coins, amount)
        self.assertEqual(1, res)

    def test_min_coin_change_2(self):
        amount = 11
        coins = [1, 2, 5]
        res = self.coin_change.get_min_coins(coins, amount)
        self.assertEqual(3, res)

    def test_min_coin_change_3(self):
        amount = 3
        coins = [2]
        res = self.coin_change.get_min_coins(coins, amount)
        self.assertEqual(-1, res)

    def test_min_coin_change_4(self):
        amount = 0
        coins = [1]
        res = self.coin_change.get_min_coins(coins, amount)
        self.assertEqual(0, res)


if __name__ == '__main__':
    unittest.main()
