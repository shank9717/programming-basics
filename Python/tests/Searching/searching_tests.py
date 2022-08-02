import unittest
from typing import List
from unittest import TestCase

from Algorithms.Searching.searcher import Searcher
from Algorithms.Searching.searching_factory import SearchingFactory, NumberSearchingAlgorithm


class TestSearchingAlgorithms(TestCase):

    def setUp(self) -> None:
        self.searching_classes: List[Searcher] = [
            SearchingFactory.get_search(NumberSearchingAlgorithm.LINEAR_SEARCH),
            SearchingFactory.get_search(NumberSearchingAlgorithm.BINARY_SEARCH)
        ]

    def test_search_single_value(self):
        array = [34]
        target = 34
        for searcher in self.searching_classes:
            index = searcher.search(array, target)
            self.assertEqual(0, index)

    def test_search_single_value_not_found(self):
        array = [34]
        target = 98
        for searcher in self.searching_classes:
            index = searcher.search(array, target)
            self.assertEqual(-1, index)

    def test_binary_search_in_sorted_array(self):
        array = [1, 10, 90, 544, 900]
        target = 90
        searcher = self.searching_classes[1]

        index = searcher.search(array, target)
        self.assertEqual(2, index)

    def test_binary_search_in_sorted_array_not_found(self):
        array = [1, 10, 90, 544, 900]
        target = 45
        searcher = self.searching_classes[1]

        index = searcher.search(array, target)
        self.assertEqual(-1, index)

    def test_linear_search_in_unsorted_array(self):
        array = [50, 1, 44, 55, 90]
        target = 90
        searcher = self.searching_classes[1]

        index = searcher.search(array, target)
        self.assertEqual(4, index)


if __name__ == '__main__':
    unittest.main()
