class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return sum([list(itertools.combinations(nums, i)) for i in xrange(len(nums) + 1)], [])
