import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.UnboundedKnapsack.coin_change_permutations import CoinChangePermutations


class TestCoinChangePermutations(TestCase):
    def setUp(self) -> None:
        self.coin_change = CoinChangePermutations()

    def test_permutations_1(self):
        amount = 5
        coins = [1, 2, 5]
        res = self.coin_change.get_permutations(coins, amount)
        self.assertEqual(9, res)

    def test_permutations_2(self):
        amount = 11
        coins = [1, 2, 5]
        res = self.coin_change.get_permutations(coins, amount)
        self.assertEqual(218, res)

    def test_permutations_3(self):
        amount = 4
        coins = [1, 2, 3]
        res = self.coin_change.get_permutations(coins, amount)
        self.assertEqual(7, res)

    def test_permutations_4(self):
        amount = 3
        coins = [9]
        res = self.coin_change.get_permutations(coins, amount)
        self.assertEqual(0, res)


if __name__ == '__main__':
    unittest.main()
