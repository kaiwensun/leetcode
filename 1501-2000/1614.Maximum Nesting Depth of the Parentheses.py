class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = cur = 0
        for c in s:
            if c == "(":
                cur += 1
                res = max(res, cur)
            elif c == ")":
                cur -= 1
        return res

