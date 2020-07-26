class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        pointers = [None] * len(nums)
        sizes = [1] * len(nums)
        for i in xrange(len(nums) - 1, -1, -1):
            for multiple_candidate_j in xrange(i + 1, len(nums)):
                if nums[multiple_candidate_j] % nums[i] == 0:
                    if sizes[multiple_candidate_j] + 1 > sizes[i]:
                        sizes[i] = sizes[multiple_candidate_j] + 1
                        pointers[i] = multiple_candidate_j
        maximum_index = max((v, i) for i, v in enumerate(sizes))[1]
        result = []
        while maximum_index is not None:
            result.append(nums[maximum_index])
            maximum_index = pointers[maximum_index]
        return result
