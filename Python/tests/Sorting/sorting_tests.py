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
            factory.get_sort(SortingAlgorithm.HEAP_SORT)
        ]

    def test_sort_single_value(self):
        array = [34]
        expected_array = [34]
        for sorter in self.sorting_classes:
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_two_values(self):
        array = [34, 10]
        expected_array = [10, 34]
        for sorter in self.sorting_classes:
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_sorted(self):
        array = [10, 34, 99]
        expected_array = [10, 34, 99]
        for sorter in self.sorting_classes:
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_reverse_sorted(self):
        array = [99, 34, 10]
        expected_array = [10, 34, 99]
        for sorter in self.sorting_classes:
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)

    def test_sort_multiple_values_mixed(self):
        array = [1, 43, 90, 11, 40, 5, 6]
        expected_array = [1, 5, 6, 11, 40, 43, 90]
        for sorter in self.sorting_classes:
            array = sorter.sort(array)
            self.assertEqual(array, expected_array)


if __name__ == '__main__':
    unittest.main()
