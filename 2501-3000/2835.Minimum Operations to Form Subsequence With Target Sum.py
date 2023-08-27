from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        cnt = Counter(nums)
        res = 0
        bit = 1
        unused = 0
        while target or cnt[bit] < 0:
            if target & bit:
                cnt[bit] -= 1
                target -= bit
            if cnt[bit] < 0:
                if unused >= -cnt[bit] * bit:
                    unused += cnt[bit] * bit
                    cnt[bit] = 0
                else:
                    borrow = (-cnt[bit] + 1) // 2
                    cnt[bit << 1] -= borrow
                    cnt[bit] += borrow * 2
                    res += borrow
            unused += cnt[bit] * bit
            bit <<= 1
        return res

