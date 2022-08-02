import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.Oor1Knapsack.equal_subset_partition import EqualSubsetPartition


class TestEqualSubsetPartitionProblem(TestCase):
    def setUp(self) -> None:
        self.partitioner = EqualSubsetPartition()

    def test_equal_subset_partition_1(self):
        can_partition = self.partitioner.can_partition([1, 2, 3, 4])
        self.assertEqual(True, can_partition)

    def test_equal_subset_partition_2(self):
        can_partition = self.partitioner.can_partition([1, 1, 3, 4, 7])
        self.assertEqual(True, can_partition)

    def test_equal_subset_partition_3(self):
        can_partition = self.partitioner.can_partition([2, 3, 4, 6])
        self.assertEqual(False, can_partition)

    def test_equal_subset_partition_4(self):
        can_partition = self.partitioner.can_partition([2, 3, 4, 5])
        self.assertEqual(True, can_partition)

    def test_equal_subset_partition_5(self):
        can_partition = self.partitioner.can_partition([2, 3, 4, 1])
        self.assertEqual(True, can_partition)

    def test_equal_subset_partition_6(self):
        can_partition = self.partitioner.can_partition([11])
        self.assertEqual(False, can_partition)

    def test_equal_subset_partition_7(self):
        can_partition = self.partitioner.can_partition([10, 5])
        self.assertEqual(False, can_partition)

    def test_equal_subset_partition_8(self):
        can_partition = self.partitioner.can_partition([100, 30, 70])
        self.assertEqual(True, can_partition)

    def test_equal_subset_partition_9(self):
        can_partition = self.partitioner.can_partition([2, 1, 1])
        self.assertEqual(True, can_partition)

    def test_equal_subset_partition_10(self):
        can_partition = self.partitioner.can_partition([5, 10, 3, 1, 1])
        self.assertEqual(True, can_partition)


if __name__ == '__main__':
    unittest.main()
