from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        res = 0
        for num in nums:
            res += cnt[num - k] + cnt[num + k]
            cnt[num] += 1
        return res

