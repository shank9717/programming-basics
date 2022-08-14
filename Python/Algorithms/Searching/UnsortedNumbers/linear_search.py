from typing import List

from Algorithms.Searching.searcher import Searcher


class LinearSearch(Searcher):

    def search(self, array: List, target: int) -> int:
        for idx in range(len(array)):
            if array[idx] == target:
                return idx
        else:
            return -1