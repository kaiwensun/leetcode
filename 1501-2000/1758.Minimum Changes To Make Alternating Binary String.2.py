class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = float("inf")
        for start in (0, 1):
            cnt = 0
            wanted = start
            for c in s:
                if c != str(wanted):
                    cnt += 1
                wanted ^= 1
            res = min(res, cnt)
        return res

