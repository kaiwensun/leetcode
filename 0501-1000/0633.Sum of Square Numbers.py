import math, bisect

squares = [0]

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in xrange(int(math.sqrt(c)) + 1):
            if math.sqrt(c - a * a).is_integer():
                return True
        return False

