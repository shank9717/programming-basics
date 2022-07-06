import math
from typing import List

from Algorithms.Sorting.counting_sort import CountingSort
from Algorithms.Sorting.sorter import Sorter


class RadixSort(Sorter):
    # Average time complexity is O(n + d) where n is size of arr and d is range of digits
    def sort(self, array: List) -> List:
        max_num = max(array)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max_num / exp > 0:
            sorter = CountingSort()
            array = sorter.sort([int((num/exp) % 10) for num in array])
            exp *= 10

        return array

    @staticmethod
    def counting_sort_alternate(arr: List, exp: int) -> List:
        max_num = len(arr)
        count_arr = [0] * max_num
        count = [0] * 10

        for i in range(max_num):
            index = arr[i] / exp
            count[int(index % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = max_num - 1
        while i >= 0:
            index = arr[i] / exp
            count_arr[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = count_arr[i]

        return arr