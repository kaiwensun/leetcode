from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dominant, cnt = Counter(nums).most_common(1)[0]
        left = 0
        for i, num in enumerate(nums):
            if dominant == num:
                left += 1
                if left * 2 > i + 1 and (cnt - left) * 2 > len(nums) - 1 - i:
                    return i
        return -1

