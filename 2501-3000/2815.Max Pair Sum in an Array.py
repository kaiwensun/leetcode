from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        group = defaultdict(list)
        for num in nums:
            group[max(map(int, str(num)))].append(num)
        res = -1
        for lst in group.values():
            lst.sort()
            if len(lst) > 1:
                res = max(res, lst[-1] + lst[-2])
        return res

