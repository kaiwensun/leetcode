from collections import Counter

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        right = Counter()
        res = 0
        for c in range(len(nums)):
            for d in range(c + 1, len(nums)):
                right[nums[d] - nums[c]] += 1
        for b in range(len(nums)):
            c = b
            for d in range(c + 1, len(nums)):
                right[nums[d] - nums[c]] -= 1
            for a in range(b):
                sm = nums[a] + nums[b]
                if sm in right:
                    res += right[sm]
        return res

