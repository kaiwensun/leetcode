class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cands = [0] * 3
        for num in nums:
            shift = num % 3
            new_cands = cands[-shift:] + cands[:-shift]
            cands = [max(cands[i], (new_cands[i] + num) if (new_cands[i] + num) % 3 == i else 0) for i in xrange(3)]
        return cands[0]
