from typing import List
from unittest import TestCase
import unittest
from Algorithms.Sorting.sorter import Sorter

from Algorithms.Sorting.sorting_factory import SortingAlgorithm, SortingFactory


class TestSortingAlgorithms(TestCase):

    def setUp(self) -> None:
        factory = SortingFactory()
        self.sorting_classes: List[Sorter] = [
            factory.get_sort(SortingAlgorithm.BUBBLE_SORT),
            factory.get_sort(SortingAlgorithm.SELECTION_SORT),
            factory.get_sort(SortingAlgorithm.INSERTION_SORT),
            factory.get_sort(SortingAlgorithm.MERGE_SORT),
            factory.get_sort(SortingAlgorithm.QUICK_SORT),
            factory.get_sort(SortingAlgorithm.HEAP_SORT),
            factory.get_sort(SortingAlgorithm.COUNTING_SORT),
            # factory.get_sort(SortingAlgorithm.RADIX_SORT)
        ]

    def test_sort_single_value(self):
        expected_array = [34]
        for sorter in self.sorting_classes:
            array = [34]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_two_values(self):
        expected_array = [10, 34]
        for sorter in self.sorting_classes:
            array = [34, 10]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_sorted(self):
        expected_array = [10, 34, 99]
        for sorter in self.sorting_classes:
            array = [10, 34, 99]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_reverse_sorted(self):
        expected_array = [10, 34, 99]
        for sorter in self.sorting_classes:
            array = [99, 34, 10]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_mixed_1(self):
        expected_array = [1, 5, 6, 11, 40, 43, 90]
        for sorter in self.sorting_classes:
            array = [1, 43, 90, 11, 40, 5, 6]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_mixed_2(self):
        expected_array = [0, 1, 5, 6, 11, 40, 43]
        for sorter in self.sorting_classes:
            array = [1, 5, 6, 11, 40, 43, 0]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_mixed_with_duplicates(self):
        expected_array = [1, 2, 3, 10, 21, 40, 40, 60]
        for sorter in self.sorting_classes:
            array = [21, 10, 40, 3, 40, 2, 60, 1]
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)


if __name__ == '__main__':
    unittest.main()
