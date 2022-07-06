import math
from typing import List

from Algorithms.Sorting.sorter import Sorter


class CountingSort(Sorter):
    # This has a time complexity of O(M + N), where M is max element (range of arr) and N is size of array
    # find_max has O(N) complexity
    # for loops have O(N) and O(M) complexity respectively
    # But this has huge space complexity (requires array of max(array) elements)
    def sort(self, array: List) -> List:
        max_num = self.find_max(array)
        new_arr = [0] * (max_num + 1)
        for num in array:
            new_arr[num] += 1

        arr_idx = 0
        for idx, value in enumerate(new_arr):
            for repetitions in range(value):
                array[arr_idx] = idx
                arr_idx += 1

        return array

    @staticmethod
    def find_max(array: List):
        max_num = -1 * math.inf
        for num in array:
            if num > max_num:
                max_num = num
        return max_num
        # Simple python code
        # return max(array)