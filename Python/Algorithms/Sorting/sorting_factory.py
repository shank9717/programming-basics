from enum import Enum
from typing import List

from Algorithms.Sorting.bubble_sort import BubbleSort
from Algorithms.Sorting.insertion_sort import InsertionSort
from Algorithms.Sorting.merge_sort import MergeSort
from Algorithms.Sorting.quick_sort import QuickSort
from Algorithms.Sorting.selection_sort import SelectionSort
from Algorithms.Sorting.heap_sort import HeapSort
from Algorithms.Sorting.counting_sort import CountingSort
from Algorithms.Sorting.radix_sort import RadixSort


class SortingAlgorithm(Enum):
    SELECTION_SORT = 1
    BUBBLE_SORT = 2
    INSERTION_SORT = 3
    MERGE_SORT = 4
    QUICK_SORT = 5
    HEAP_SORT = 6
    COUNTING_SORT = 7
    RADIX_SORT = 8

class SortingFactory():
    def __init__(self):
        pass

    def get_sort(self, sort_method: SortingAlgorithm) -> Sorter:
        if sort_method == SortingAlgorithm.BUBBLE_SORT:
            return BubbleSort()
        elif sort_method == SortingAlgorithm.SELECTION_SORT:
            return SelectionSort()
        elif sort_method == SortingAlgorithm.INSERTION_SORT:
            return InsertionSort()
        elif sort_method == SortingAlgorithm.MERGE_SORT:
            return MergeSort()
        elif sort_method == SortingAlgorithm.QUICK_SORT:
            return QuickSort()
        elif sort_method == SortingAlgorithm.HEAP_SORT:
            return HeapSort()
        # elif sort_method == SortingAlgorithm.COUNTING_SORT:
        #     return CountingSort()
        # elif sort_method == SortingAlgorithm.RADIX_SORT:
        #     return RadixSort()
        else:
            raise ValueError("Invalid sorting algorithm")

class Sorter():
    def sort(self, array: List):
        raise NotImplementedError()
    
    def swap(self, array: List, idx1: int, idx2: int):
        array[idx1], array[idx2] = array[idx2], array[idx1]