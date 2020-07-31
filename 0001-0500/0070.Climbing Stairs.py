class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        yesterday, today = 0, 1
        for i in xrange(n):
            yesterday, today = today, yesterday + today
        return today

