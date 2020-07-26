class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        MOD = 10 ** 9 + 7
        PRIME = 97
        orda = ord('a')
        if len(s) <= 1:
            return ""
        def get_hash(start, end):
            res = 0
            for i in xrange(start, end + 1):
                res = (res * PRIME + (ord(s[i]) - orda)) % MOD
            return res
        acc_primes = [1] * len(s)
        for i in xrange(1, len(s)):
            acc_primes[i] = (acc_primes[i - 1] * PRIME) % MOD
        prefix_hash = get_hash(0, len(s) - 2)
        suffix_hash = get_hash(1, len(s) - 1)
        mx_length = len(s) - 1
        def delete_prefix_tail(prefix_hash, i):
            return (prefix_hash - (ord(s[i]) - orda) * acc_primes[len(s) - 2 - i]) % MOD
        def delete_suffix_head(suffix_hash, i):
            return (((suffix_hash - (ord(s[i]) - orda) * acc_primes[len(s) - 2]) % MOD) * PRIME) % MOD
        for i in xrange(0, len(s) - 1):
            if prefix_hash == suffix_hash:
                if s[:mx_length - i] == s[-mx_length + i:]:
                    return s[:mx_length - i]
            prefix_hash = delete_prefix_tail(prefix_hash, len(s) - 2 - i)
            suffix_hash = delete_suffix_head(suffix_hash, i + 1)
        return ""
