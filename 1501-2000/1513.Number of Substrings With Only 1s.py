MOD = 10 ** 9 + 7
class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        last_zero = -1
        for i in xrange(len(s)):
            if s[i] == '0':
                last_zero = i
            else:
                res += i - last_zero
                res %= MOD
        return res
