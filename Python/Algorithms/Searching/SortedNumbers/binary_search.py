from typing import List

from Algorithms.Searching.searcher import Searcher


class BinarySearch(Searcher):

    def search(self, array: List, target: int) -> int:
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == target:
                # Found number
                return mid
            elif array[mid] > target:
                # Mid lies on right of target. Search on left side of array
                high = mid - 1
            else:
                # Mid lies on left of target. Search on right side of array
                low = mid + 1

        # Not found
        return -1