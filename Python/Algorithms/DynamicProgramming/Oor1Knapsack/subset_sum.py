"""
Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given number ‘S’.

Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
"""
from typing import List, Dict, Tuple


class SubsetSum:
    def check_subset_sum(self, numbers: List[int], target: int) -> bool:
        return self.subset_sum(numbers, target, memo={})

    def subset_sum(self, numbers: List[int], target: int,
                   idx: int = 0, current_sum: int = 0, memo: Dict[Tuple[int, int], bool] = {}) -> bool:
        if (idx, current_sum) in memo:
            return memo[(idx, current_sum)]
        if current_sum == target:
            memo[(idx, current_sum)] = True
            return True
        if idx >= len(numbers):
            memo[(idx, current_sum)] = False
            return False

        pick_subset_sum = self.subset_sum(numbers, target, idx + 1, current_sum + numbers[idx], memo)
        if pick_subset_sum:
            memo[(idx, current_sum)] = True
            return True
        leave_subset_sum = self.subset_sum(numbers, target, idx + 1, current_sum, memo)
        if leave_subset_sum:
            memo[(idx, current_sum)] = True
            return True

        memo[(idx, current_sum)] = False
        return False
