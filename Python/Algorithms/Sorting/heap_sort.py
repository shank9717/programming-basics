from typing import List

from Algorithms.Sorting.sorter import Sorter
from DataStructures.heap import MaxHeap


class HeapSort(Sorter):
    def sort(self, array: List) -> List:
        array_size = len(array)
        heap = MaxHeap(array)
        heap.build_max_heap()
        new_arr = []
        for _ in range(array_size):
            new_arr.append(heap.extract_max())
        return new_arr