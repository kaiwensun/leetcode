from collections import Counter

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        def test(window_size, scan_full=False):
            cnt = Counter()
            mx = 0
            for i, num in enumerate(nums):
                cnt[num] += 1
                if i >= window_size:
                    cnt[nums[i - window_size]] -= 1
                mx = max(mx, cnt[num])
                if not scan_full and mx + k >= window_size:
                    return True, mx
            return False, mx
        l, r = 0, len(nums) + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid)[0]:
                l = mid + 1
            else:
                r = mid
        return test(l - 1, True)[1]

