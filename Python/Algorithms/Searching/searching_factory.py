from enum import Enum

from Algorithms.Searching.SortedNumbers.binary_search import BinarySearch
from Algorithms.Searching.UnsortedNumbers.linear_search import LinearSearch
from Algorithms.Searching.searcher import Searcher


class NumberSearchingAlgorithm(Enum):
    LINEAR_SEARCH = 1
    BINARY_SEARCH = 2

class SearchingFactory:

    @staticmethod
    def get_search(search_method: NumberSearchingAlgorithm) -> Searcher:
        if search_method == NumberSearchingAlgorithm.LINEAR_SEARCH:
            return LinearSearch()
        elif search_method == NumberSearchingAlgorithm.BINARY_SEARCH:
            return BinarySearch()
        else:
            raise ValueError("Invalid sorting algorithm")
