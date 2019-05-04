class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        farthest = 0
        for i in xrange(len(nums)):
            for j in xrange(max(farthest + 1, i + 1), min(len(nums), i + 1 + nums[i])):
                dp[j] = min(dp[i] + 1, dp[j])
                farthest = max(farthest, j)
        return dp[-1]
                
