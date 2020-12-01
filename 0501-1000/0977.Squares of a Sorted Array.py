from bisect import bisect_right
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = bisect_right(nums, 0)
        l = r - 1
        INF = float("inf")
        res = []
        while r - l <= len(nums):
            lnum = nums[l] if l >= 0 else -INF
            rnum = nums[r] if r < len(nums) else INF
            if -lnum < rnum:
                res.append(lnum ** 2)
                l -= 1
            else:
                res.append(rnum ** 2)
                r += 1
        return res

