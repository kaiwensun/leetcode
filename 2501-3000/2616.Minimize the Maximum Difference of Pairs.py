class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        diffs = [abs(d[0] - d[1]) for d in zip(nums[1:], nums[:-1])]
        def test(diff):
            i = cnt = 0
            while i < len(diffs):
                if diffs[i] <= diff:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        l, r = 0, max(diffs) + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                r = mid
            else:
                l = mid + 1
        return l

