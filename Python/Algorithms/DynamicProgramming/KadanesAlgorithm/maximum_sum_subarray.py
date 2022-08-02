# This is an optimized version of brute force O(n^2) solution
from typing import List


class MaximumSumSubarray:
    @staticmethod
    def max_sum(arr: List[int]):
        local_max = 0
        global_max = float('-inf')

        for number in arr:
            local_max = max(number, local_max + number)
            if local_max > global_max:
                global_max = local_max

        return global_max
