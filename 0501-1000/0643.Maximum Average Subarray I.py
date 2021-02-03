class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = float("-inf")
        l = cur = 0
        for r in xrange(len(nums)):
            cur += nums[r]
            if r - l + 1 > k:
                cur -= nums[l]
                l += 1
            if r + 1 >= k:
                res = max(res, cur)
        return res / float(k)

