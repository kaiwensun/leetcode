#Basic Idea:
# Hashset
#Result:
# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 54.32% of python submissions.
#Date:
# 9/21/2016

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in xrange(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]],i]
            d[nums[i]]=i
        return None
        
