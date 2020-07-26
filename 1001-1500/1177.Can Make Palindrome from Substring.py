from collections import Counter
class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def countBit(n):
            res = 0
            while n:
                n &= (n - 1)
                res += 1
            return res

        counters = [0] * (len(s) + 1)
        counter = 0
        for index, c in enumerate(s):
            counter ^= 1 << (ord(c) - ord('a'))
            counters[index + 1] = counter
        return [countBit(counters[l] ^ counters[r + 1]) / 2 <= k for l, r, k in queries]
