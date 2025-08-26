from collections import Counter

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        return len(nums) % k == 0 and Counter(nums).most_common(1)[0][1] * k <= len(nums)

