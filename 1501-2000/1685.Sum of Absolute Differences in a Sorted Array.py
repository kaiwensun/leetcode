class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_num_index = list(sorted([(num, index) for index, num in enumerate(nums)]))
        prefix_sum = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        def get_prefix_sum(i):
            return prefix_sum[i + 1]
        def get_suffix_sum(i):
            return prefix_sum[-1] - prefix_sum[i]

        res = [None] * len(nums)
        for j, (num, original_index) in enumerate(sorted_num_index):
            res[original_index] = (num * j - get_prefix_sum(original_index - 1)) + (get_suffix_sum(original_index + 1) - num * (len(nums) - 1 - j))
        return res

