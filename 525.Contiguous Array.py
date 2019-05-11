class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnts = [0, 0]
        earliestDiff2Index = {0 : -1}
        res = 0
        for index, num in enumerate(nums):
            cnts[num] += 1
            diff = cnts[0] - cnts[1]
            res = max(res, index - earliestDiff2Index.setdefault(diff, index))
        return res
