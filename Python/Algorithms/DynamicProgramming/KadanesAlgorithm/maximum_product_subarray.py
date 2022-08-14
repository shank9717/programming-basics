# This is an optimized version of brute force O(n^2) solution
from typing import List


class MaximumProductSubarray:
    @staticmethod
    def max_product(nums: List[int]):
        product = 1
        result = (-10**4) - 1
        for num in nums:
            product = product * num
            result = max(result, product)
            if product == 0:
                product = 1

        product = 1

        for num in nums[::-1]:
            product = product * num
            result = max(result, product)
            if product == 0:
                product = 1

        return result
