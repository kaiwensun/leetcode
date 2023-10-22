from collections import Counter

class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        counts = sorted(Counter(nums).values())
        def test(limit):
            res = 0
            for count in counts:
                multi = (count + limit - 1) // limit
                if multi * (limit - 1) <= count:
                    res += multi
                else:
                    return None
            return res
        for limit in range(counts[0] + 1, -1, -1):
            res = test(limit)
            if res is not None:
                return res

