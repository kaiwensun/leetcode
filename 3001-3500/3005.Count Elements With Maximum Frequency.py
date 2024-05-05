from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums).most_common()
        return sum([p[1] for p in cnt if p[1] == cnt[0][1]])

