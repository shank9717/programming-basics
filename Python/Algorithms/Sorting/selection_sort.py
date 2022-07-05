from typing import List

from Algorithms.Sorting.sorting_factory import Sorter


class SelectionSort(Sorter):
    def sort(self, array: List):
        array_size = len(array)
        for firstIdx in range(array_size - 1):
            minIdx = firstIdx
            for secondIdx in range(firstIdx + 1, array_size):
                if array[secondIdx] < array[minIdx]:
                    minIdx = secondIdx
            self.swap(array, firstIdx, minIdx)