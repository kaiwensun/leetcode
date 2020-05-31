class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getBiggestTwo(nums, converter):
            fst = snd = float('-inf')
            for num in nums:
                numc = converter(num)
                if numc > fst:
                    snd = fst
                    fst = numc
                elif numc > snd:
                    snd = numc
            return fst, snd
        biggests = getBiggestTwo(nums, lambda x: x - 1)
        smallests = getBiggestTwo(nums, lambda x: -(x - 1))
        return max(biggests[0] * biggests[1], smallests[0] * smallests[1])
        
        # # Brute force:
        #
        # res = float('-inf')
        # for i in xrange(len(nums)):
        #     for j in xrange(i + 1, len(nums)):
        #         res = max(res, (nums[i] - 1) * (nums[j] - 1))
        # return res
