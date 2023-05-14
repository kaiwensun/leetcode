from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        left = Counter()
        right = Counter(nums)
        res = []
        for num in nums:
            left[num] += 1
            right[num] -= 1
            if right[num] == 0:
                del right[num]
            res.append(len(left) - len(right))
        return res

