class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = neg = res = float('-inf')
        for num in nums:
            if num == 0:
                pos = neg = float('-inf')
            else:
                pos = max(0, pos)
                if num < 0:
                    pos, neg = neg, pos
                pos += 1
                neg += 1
            res = max(res, pos)
        return max(0, res)
