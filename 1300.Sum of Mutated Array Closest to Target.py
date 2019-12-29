class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        def calcSum(value):
            index = bisect.bisect_right(arr, value)
            return prefix[index] + (len(arr) - index) * value
        arr = sorted(arr)
        prefix = [0] * (len(arr) + 1)
        for i in xrange(len(arr)):
            prefix[i + 1] = prefix[i] + arr[i]
        lo, hi = 0, arr[-1] + 1
        min_diff = float('inf')
        opt_value = float('inf')
        while lo < hi:
            mid = (lo + hi) / 2
            s = calcSum(mid)
            diff = abs(s - target)
            if diff <= min_diff:
                opt_value = min(opt_value, mid) if diff == min_diff else mid
                min_diff = diff
            if target <= s:
                hi = mid
            else:
                lo = mid + 1
        return opt_value
