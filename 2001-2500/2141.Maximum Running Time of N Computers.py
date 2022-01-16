class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        B = len(batteries)
        if B < n:
            return 0
        if B == n:
            return min(batteries)
        batteries.sort()
        presum = [0] * (len(batteries) + 1)
        for i in range(B):
            presum[i + 1] = batteries[i] + presum[i]

        def test(minute):
            i = bisect.bisect_left(batteries, minute)
            if i == 0:
                return True
            return (n - (B - i)) * minute <= presum[i]

        l, r = 0, presum[-1] // n + 1
        while l < r:
            mid = (l + r) // 2
            if test(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

