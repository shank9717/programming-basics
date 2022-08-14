import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.UnboundedKnapsack.rod_cutting_problem import RodCutting


class TestRodCuttingProblem(TestCase):
    def setUp(self) -> None:
        self.rod_cutter = RodCutting()

    def test_rod_cutting_1(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20]
        res = self.rod_cutter.max_price(prices)
        self.assertEqual(22, res)

    def test_rod_cutting_2(self):
        prices = [3, 5, 8, 9, 10, 17, 17, 20]
        res = self.rod_cutter.max_price(prices)
        self.assertEqual(24, res)

    def test_rod_cutting_3(self):
        prices = [1, 1]
        res = self.rod_cutter.max_price(prices)
        self.assertEqual(2, res)

    def test_rod_cutting_4(self):
        prices = [1, 100, 1000]
        res = self.rod_cutter.max_price(prices)
        self.assertEqual(1000, res)

    def test_rod_cutting_5(self):
        prices = [65]
        res = self.rod_cutter.max_price(prices)
        self.assertEqual(65, res)


if __name__ == '__main__':
    unittest.main()
