class Solution(object):
    def maximumScore(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        row = sorted([a, b, c])
        res = 0
        while row[1] != 0:
            res += 1
            row[1] -= 1
            row[2] -= 1
            row.sort()
        return res

