class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lengths = [None] * len(nums)
        cnts = [None] * len(nums)
        for i in xrange(len(nums)):
            mx_cnt = 0
            mx = float('-inf')
            for j in xrange(i):
                if nums[j] < nums[i]:
                    if lengths[j] > mx:
                        mx_cnt = 0
                        mx = lengths[j]
                    if lengths[j] == mx:
                        mx_cnt += cnts[j]
            cnts[i] = mx_cnt or 1
            lengths[i] = mx + 1 if mx_cnt else 1
        mx_lengths = max(lengths or [0])
        return sum(cnts[i] for i in xrange(len(nums)) if lengths[i] == mx_lengths)    
