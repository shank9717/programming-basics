from typing import List

from Algorithms.Sorting.sorting_factory import Sorter
from DataStructures.heap import MaxHeap


class HeapSort(Sorter):
    def sort(self, array: List):
        heap = MaxHeap(array)
        heap.build_max_heap()
        for idx in range(len(array)):
            array[idx] = heap.extract_max()
        return array