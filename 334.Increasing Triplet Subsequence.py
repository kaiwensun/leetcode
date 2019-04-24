class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1 = float('inf')
        m2 = float('inf')
        for num in nums:
            if m1 < m2 < num:
                return True
            if num < m1:
                m1 = num
            elif m1 < num < m2:
                m2 = num
        return False
