from collections import Counter

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        MAX = 2 ** 31
        bit = 1
        cnt = Counter()
        while bit < MAX:
            for num in nums:
                cnt[num & bit] += 1
            bit <<= 1
        res = 0
        bit = 1
        while bit < MAX:
            if cnt[bit] >= k:
                res |= bit
            bit <<= 1
        return res

