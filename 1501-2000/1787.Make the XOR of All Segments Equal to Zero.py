from functools import lru_cache
from collections import Counter

"""
Idea:
Given [1,2,4,1,2,5,1,2,6, 8], k = 3
Convert the line [1,2,4,1,2,5,1,2,6, 8] into matrix:
    [
        [1,2,4],
        [1,2,5],
        [1,2,6],
        [b]
    ]
There are two strategies:
1. Each column can be all changed to a number EXISTING in this column
2. Pick one column to change all numbers into an arbitrary number, the other columns spend their minimum costs to unify the column.
The final cost is the minimum costs derived from the two strategies.
"""
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:

        counters = [Counter() for _ in range(k)]
        for i, num in enumerate(nums):
            counters[i % k][num] += 1

        def count_column_size(i):
            last_line_size = len(nums) % k
            return len(nums) // k + int(i % k + 1 <= len(nums) % k)

        @lru_cache(None)
        def dfs(i, expected):
            if i == k:
                return 0 if expected == 0 else float("inf")
            total = count_column_size(i)
            min_cost = float("inf")
            for num, unchanged_cnt in counters[i].items():
                min_cost = min(min_cost, total - unchanged_cnt + dfs(i + 1, expected ^ num))
            return min_cost

        # min cost of strategy 1
        min_cost = dfs(0, 0)
        min_unify_cost = sum(count_column_size(i) - max(counters[i].values()) for i in range(k))
        i = 0
        # min cost of strategy 2
        for i in range(k):
            min_cost = min(min_cost, min_unify_cost + max(counters[i].values()))
        return min_cost

