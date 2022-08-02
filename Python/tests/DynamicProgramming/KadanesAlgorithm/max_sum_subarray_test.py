import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.KadanesAlgorithm.maximum_sum_subarray import MaximumSumSubarray


class TestMaximumSumSubarray(TestCase):
    def setUp(self) -> None:
        self.mss = MaximumSumSubarray()

    def test_max_sum_subarray_1(self):
        self.assertEqual(6, self.mss.max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_max_sum_subarray_2(self):
        self.assertEqual(-2, self.mss.max_sum([-2]))

    def test_max_sum_subarray_3(self):
        self.assertEqual(3, self.mss.max_sum([3]))

    def test_max_sum_subarray_4(self):
        self.assertEqual(13, self.mss.max_sum([-13, 13]))

    def test_max_sum_subarray_5(self):
        self.assertEqual(15, self.mss.max_sum([10, -15, 15]))

    def test_max_sum_subarray_6(self):
        self.assertEqual(25, self.mss.max_sum([10, 15, -15]))

    def test_max_sum_subarray_7(self):
        self.assertEqual(7, self.mss.max_sum([-2, -3, 4, -1, -2, 1, 5, -3]))


if __name__ == '__main__':
    unittest.main()
