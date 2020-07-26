class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        state = '0'
        res = 0
        for b in target:
            if state != b:
                state = b
                res += 1
        return res