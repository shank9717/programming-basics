"""
Given two integer arrays to represent weights and profits of ‘N’ items,
we need to find a subset of these items which will give us maximum profit such that their cumulative weight
is not more than a given number ‘C’. Write a function that returns the maximum profit. Each item can only be
selected once, which means either we put an item in the knapsack or skip it.

Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’.
The goal is to get the maximum profit from the items in the knapsack.
Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit.
Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put different combinations of fruits in the knapsack, such that their total weight is not more than 5:

Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit

This shows that Banana + Melon is the best combination,
as it gives us the maximum profit and the total weight does not exceed the capacity.
"""
from typing import List, Dict, Tuple


class Knapsack:
    def maximum_profit(self, weights: List[int], profits: List[int], capacity: int) -> int:
        return self.get_max_profit(weights, profits, capacity, dp={})

    def get_max_profit(self, weights: List[int], profits: List[int], capacity: int, idx: int = 0,
                       current_weight: int = 0, dp: Dict[Tuple[int, int], int] = {}) -> int:
        if (current_weight, idx) in dp:
            return dp[(current_weight, idx)]

        if idx >= len(weights):
            return 0

        take_item_weight = current_weight + weights[idx]
        take_item_profit = 0
        if take_item_weight <= capacity:
            take_item_profit = profits[idx] + self.get_max_profit(weights, profits, capacity, idx + 1, take_item_weight,
                                                                  dp)
        leave_item_profit = self.get_max_profit(weights, profits, capacity, idx + 1, current_weight, dp)
        current_profit = max(take_item_profit, leave_item_profit)
        dp[(current_weight, idx)] = current_profit
        return current_profit
