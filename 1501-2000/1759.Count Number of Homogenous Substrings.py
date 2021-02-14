class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        l = res = 0
        for r in xrange(len(s)):
            if s[r] != s[l]:
                l = r
            res += r - l + 1
            res %= MOD
        return res

