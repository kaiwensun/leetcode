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
        if row[0] + row[1] <= row[2]:
            return row[0] + row[1]
        while row[1] != 0:
            if row[0] == row[1] == row[2]:
                res += row[0] * 3 // 2
                break
            diff = (row[1] - row[0]) or (row[2] - row[1])
            res += diff
            row[2] -= diff
            row[1] -= diff
            row.sort()
        return res

