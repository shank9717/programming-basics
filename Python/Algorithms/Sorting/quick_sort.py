from typing import List

from Algorithms.Sorting.sorting_factory import Sorter


class QuickSort(Sorter):
    def sort(self, array: List):
        array_size = len(array)
        self.quick_sort(array, 0, array_size)

    def quick_sort(self, array: List, low: int, high: int):
        if low < high:
            partition_index = self.partition(array, low, high)
            self.quick_sort(array, low, partition_index - 1)
            self.quick_sort(array, partition_index + 1, high)

    def partition(self, array: List, low: int, high: int):
        pivot = array[high]
        ptr = low - 1
        for idx in range(low, high):
            if array[idx] <= pivot:
                ptr += 1
                array[ptr], array[idx] = array[idx], array[ptr]

        array[ptr + 1], array[high] = array[high], array[ptr + 1]
        return ptr + 1
        