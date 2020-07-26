class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(filter(lambda x : x % 2 == 0, map(len, map(str, nums))))
