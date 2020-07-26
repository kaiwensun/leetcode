class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        MOD = 10 ** 9 + 7
        PRIME = 97
        acc_prime = 1
        l, r = 0, 0
        res = ""
        for i in xrange(len(s) - 1):
            l = (l * PRIME + ord(s[i]) - ord('a')) % MOD
            r = (r + (ord(s[~i]) - ord('a')) * acc_prime) % MOD
            acc_prime = (acc_prime * PRIME) % MOD
            if l == r and s[:i + 1] == s[-i - 1:]:
                res = s[:i + 1]
        return res
