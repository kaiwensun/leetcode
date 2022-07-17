from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums).values()
        return [sum(item // 2 for item in cnt), len([item for item in cnt if item % 2])]

