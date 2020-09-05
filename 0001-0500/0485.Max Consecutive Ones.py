class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(map(lambda str : len(str), "".join(map(lambda c : str(c), nums)).split("0")))

