class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        
        def dfs(start, end):
            if start == end:
                return 0
            if start + 1 == end:
                return abs(nums[start])
            mid = (start + end) // 2
            res = max(dfs(start, mid), dfs(mid, end))
            sm = lmax = lmin = rmax = rmin = 0
            for i in xrange(mid, end):
                sm += nums[i]
                rmax = max(rmax, sm)
                rmin = min(rmin, sm)
            sm = 0
            for i in xrange(mid - 1, start - 1, -1):
                sm += nums[i]
                lmax = max(lmax, sm)
                lmin = min(lmin, sm)
            res = max(res, abs(lmin + rmin), abs(lmax + rmax))
            return res
        return dfs(0, len(nums))

