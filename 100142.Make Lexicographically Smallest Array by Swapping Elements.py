from collections import defaultdict
from bisect import bisect_right

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        key = None
        tail = float("-inf")
        groups = defaultdict(list)
        for num in sorted(nums):
            if num - tail > limit:
                key = num
            groups[key].append(num)
            tail = num
        keys = sorted(groups.keys())
        for value in groups.values():
            value.reverse()
        res = []
        for num in nums:
            key = keys[bisect_right(keys, num) - 1]
            res.append(groups[key].pop())
        return res

