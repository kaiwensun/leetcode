from collections import Counter

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter()
        res = sm = 0
        for i, num in enumerate(nums):
            cnt[num] += 1
            sm += num
            if i - k >= 0:
                prev = nums[i - k]
                sm -= prev
                cnt[prev] -= 1
                if not cnt[prev]:
                    del cnt[prev]
            if i >= k - 1:
                if len(cnt) >= m:
                    res = max(res, sm)
        return res

