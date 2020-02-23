import math
class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        num1 = num + 1
        num2 = num + 2
        mx = int(math.sqrt(num2))
        res = [[], float('inf')]
        
        def candidate(a, b, res):
            if b - a < res[1]:
                res[0] = [a, b]
                res[1] = b - a
        for a in xrange(mx, 0, -1):
            if num1 % a == 0:
                candidate(a, num1 // a, res)
            if num2 % a == 0:
                candidate(a, num2 // a, res)
        return res[0]
