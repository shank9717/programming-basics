from typing import List

from Algorithms.Sorting.sorter import Sorter


class SelectionSort(Sorter):

    # This has complexity of O(N^2) but is faster than bubble sort due to fewer swaps
    def sort(self, array: List) -> List:
        array_size = len(array)
        for firstIdx in range(array_size - 1):
            min_idx = firstIdx
            for secondIdx in range(firstIdx + 1, array_size):
                if array[secondIdx] < array[min_idx]:
                    min_idx = secondIdx
            self.swap(array, firstIdx, min_idx)
        
        return array