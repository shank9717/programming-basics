import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.Oor1Knapsack.knapsack_problem import Knapsack


class TestKnapsackProblem(TestCase):
    def setUp(self) -> None:
        self.knapsack = Knapsack()

    def test_knapsack_1(self):
        # items = ["Apple", "Orange", "Banana", "Melon"]
        weights = [2, 3, 1, 4]
        profits = [4, 5, 3, 7]
        profit = self.knapsack.maximum_profit(weights, profits, capacity=5)
        self.assertEqual(10, profit)

    def test_knapsack_2(self):
        # items = ["Apple", "Orange", "Banana", "Melon"]
        profits = [1, 6, 10, 16]
        weights = [1, 2, 3, 5]
        profit = self.knapsack.maximum_profit(weights, profits, capacity=7)
        self.assertEqual(22, profit)

        profit = self.knapsack.maximum_profit(weights, profits, capacity=6)
        self.assertEqual(17, profit)

    def test_knapsack_3(self):
        # items = ["Apple"]
        weights = [2]
        profits = [4]
        profit = self.knapsack.maximum_profit(weights, profits, capacity=2)
        self.assertEqual(4, profit)

    def test_knapsack_4(self):
        # items = ["Apple"]
        weights = [2]
        profits = [4]
        profit = self.knapsack.maximum_profit(weights, profits, capacity=1)
        self.assertEqual(0, profit)


if __name__ == '__main__':
    unittest.main()
