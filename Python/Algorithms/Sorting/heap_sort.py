from typing import List

from Algorithms.Sorting.sorter import Sorter
from DataStructures.heap import MinHeap


class HeapSort(Sorter):
    # build_min_heap is of complexity N.log(N) and extract min is of complexity log(N). Total complexity is N.log(N)
    def sort(self, array: List) -> List:
        array_size = len(array)
        heap = MinHeap(array)
        heap.build_min_heap()
        new_arr = []
        for _ in range(array_size):
            new_arr.append(heap.extract_min())
        return new_arr