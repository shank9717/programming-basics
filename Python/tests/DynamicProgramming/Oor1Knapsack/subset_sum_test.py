import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.Oor1Knapsack.subset_sum import SubsetSum


class TestSubsetSumProblem(TestCase):
    def setUp(self) -> None:
        self.subset_sum = SubsetSum()

    def test_subset_sum_1(self):
        numbers = [1, 2, 3, 7]
        target = 6
        possible = self.subset_sum.check_subset_sum(numbers, target)
        self.assertEqual(True, possible)

    def test_subset_sum_2(self):
        numbers = [1, 2, 7, 1, 5]
        target = 10
        possible = self.subset_sum.check_subset_sum(numbers, target)
        self.assertEqual(True, possible)

    def test_subset_sum_3(self):
        numbers = [1, 3, 4, 8]
        target = 6
        possible = self.subset_sum.check_subset_sum(numbers, target)
        self.assertEqual(False, possible)

    def test_subset_sum_4(self):
        numbers = [65]
        target = 65
        possible = self.subset_sum.check_subset_sum(numbers, target)
        self.assertEqual(True, possible)

    def test_subset_sum_5(self):
        numbers = []
        target = 13
        possible = self.subset_sum.check_subset_sum(numbers, target)
        self.assertEqual(False, possible)

    def test_subset_sum_6(self):
        numbers = [13, 1, 0]
        target = 13
        possible = self.subset_sum.check_subset_sum(numbers, target)
        self.assertEqual(True, possible)


if __name__ == '__main__':
    unittest.main()
