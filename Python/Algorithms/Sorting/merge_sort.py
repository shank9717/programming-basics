from typing import List

from Algorithms.Sorting.sorter import Sorter


class MergeSort(Sorter):
    def sort(self, array: List) -> List:
        array_size = len(array)
        if array_size <= 1:
            return array
        self.merge_sort(array, 0, array_size)
        return array
    
    def merge_sort(self, array: List, left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid + 1, right)
            self.merge(array, left, mid, right)

    @staticmethod
    def merge(self, array: List, left: int, mid: int, right: int) -> None:
        left_arr = array[left:mid + 1]
        right_arr = array[mid + 1:right + 1]
        left_idx, right_idx = 0, 0
        idx = left
        while left_idx < len(left_arr) and right_idx < len(right_arr):
            if left_arr[left_idx] < right_arr[right_idx]:
                array[left + idx] = left_arr[left_idx]
                left_idx += 1
            else:
                array[left + idx] = right_arr[right_idx]
                right_idx += 1
            idx += 1
        
        while left_idx < len(left_arr):
            array[left + left_idx] = left_arr[left_idx]
            left_idx += 1
        
        while right_idx < len(right_arr):
            array[left + right_idx] = right_arr[right_idx]
            right_idx += 1