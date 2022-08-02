import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.KadanesAlgorithm.maximum_product_subarray import MaximumProductSubarray


class TestMaximumProductSubarray(TestCase):
    def setUp(self) -> None:
        self.mps = MaximumProductSubarray()

    def test_max_product_subarray_1(self):
        self.assertEqual(960, self.mps.max_product([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_max_product_subarray_2(self):
        self.assertEqual(-2, self.mps.max_product([-2]))

    def test_max_product_subarray_3(self):
        self.assertEqual(3, self.mps.max_product([3]))

    def test_max_product_subarray_4(self):
        self.assertEqual(13, self.mps.max_product([-13, 13]))

    def test_max_product_subarray_5(self):
        self.assertEqual(15, self.mps.max_product([10, -15, 15]))

    def test_max_product_subarray_6(self):
        self.assertEqual(150, self.mps.max_product([10, 15, -15]))

    def test_max_product_subarray_7(self):
        self.assertEqual(360, self.mps.max_product([-2, -3, 4, -1, -2, 1, 5, -3]))


if __name__ == '__main__':
    unittest.main()
