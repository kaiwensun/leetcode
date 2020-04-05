class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        num = int(s, 2)
        while num != 1:
            if num % 2:
                num += 1
            else:
                num /= 2
            res += 1
        return res
