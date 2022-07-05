from typing import List

from Algorithms.Sorting.sorting_factory import Sorter


class BubbleSort(Sorter):
    def sort(self, array: List):
        array_size = len(array)
        for firstIdx in range(array_size - 1):
            for secondIdx in range(firstIdx, array_size - 1):
                if array[secondIdx] > array[secondIdx + 1]:
                    self.swap(array, secondIdx, secondIdx + 1)
    