class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(num for num, cnt in Counter(nums).iteritems() if cnt == 1)

