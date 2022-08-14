from typing import List

from Algorithms.Sorting.sorter import Sorter


class BubbleSort(Sorter):
    # This algorithm is of time complexity O(n^2) due to nested loop, each ranging till n
    def sort(self, array: List) -> List:
        array_size = len(array)
        for firstIdx in range(array_size - 1):
            for secondIdx in range(0, array_size - 1):
                if array[secondIdx] > array[secondIdx + 1]:
                    self.swap(array, secondIdx, secondIdx + 1)
        
        return array