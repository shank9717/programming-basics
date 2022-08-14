"""
Given a set of positive numbers,
find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

"""
from typing import List, Dict, Tuple


class EqualSubsetPartition:
    def can_partition(self, numbers: List[int]) -> bool:
        if sum(numbers) % 2 != 0:
            return False

        return self.check_partition(numbers, memo={})

    def check_partition(self, numbers: List[int], idx: int = 0, current_sum: int = 0,
                        skip_idx: List[int] = [], memo: Dict[Tuple[int, int], bool] = {}) -> bool:
        if (current_sum, idx) in memo:
            self.memo_hits += 1
            return memo[(current_sum, idx)]

        if idx >= len(numbers):
            memo[(current_sum, idx)] = False
            return False

        other_sum = 0
        for i, number in enumerate(numbers):
            if not i in skip_idx:
                other_sum += number

        if other_sum == current_sum:
            memo[(current_sum, idx)] = True
            return True

        take_idx_sum = current_sum + numbers[idx]
        leave_idx_partition = self.check_partition(numbers, idx + 1, current_sum, skip_idx, memo)
        if leave_idx_partition:
            memo[(current_sum, idx)] = True
            return True
        temp_skip = [idx for idx in skip_idx]
        temp_skip.append(idx)
        take_idx_partition = self.check_partition(numbers, idx + 1, take_idx_sum, temp_skip, memo)
        if take_idx_partition:
            memo[(current_sum, idx)] = True
            return True

        memo[(current_sum, idx)] = False
        return False
