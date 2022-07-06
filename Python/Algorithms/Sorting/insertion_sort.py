from typing import List

from Algorithms.Sorting.sorter import Sorter


class InsertionSort(Sorter):
    def sort(self, array: List) -> List:
        array_size = len(array)
        for idx in range(1, array_size):
            key = array[idx]
            position = idx - 1
            while position >= 0 and array[position] > key:
                array[position + 1] = array[position]
                position -= 1
            array[position + 1] = key
        
        return array