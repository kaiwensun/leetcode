from collections import Counter
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return Counter(nums).most_common()[0][0]

