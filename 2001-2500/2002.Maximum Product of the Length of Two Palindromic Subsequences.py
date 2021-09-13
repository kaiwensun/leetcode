import functools

class Solution:
    def maxProduct(self, s: str) -> int:

        def pbin(bits):
            b = bin(bits)[2:]
            b = ''.join(reversed('0' * (n - len(b)) + b))
            return '0b' + b

        @functools.lru_cache(1000)
        def calc_size(bits):
            res = 0
            while bits:
                bits &= (bits - 1)
                res += 1
            return res

        def is_taken(mask, bits1, bits2):
            return bool(mask & (bits1 | bits2))

        n = len(s)
        i1 = i2 = -1
        j1 = j2 = n

        @functools.cache
        def dp(p, bits1, bits2):

            res = 0
            nonlocal i1, j1, i2, j2
            freeze = [i1, j1, i2, j2]

            if bits1 > bits2:
                i1, j1, i2, j2 = i2, j2, i1, j1
                res = dp(p, bits2, bits1)
                i1, j1, i2, j2 = freeze
                return res
            if p >= j1 and p >= j2:
                return calc_size(bits1) * calc_size(bits2)

            mask = 1 << p
            if mask & (bits1 | bits2):
                return dp(p + 1, bits1, bits2)
            """
            cases:
            - as part of a pair:
                - join group1
                - join group2
            - as the middle point:
                - join group1
                - join group2
            - do not join any group
            """

            # do not join any group
            res = dp(p + 1, bits1, bits2)
            
            # as part of a pair
            for k in range(i1 + 1, j1):
                if s[k] == s[p] and not is_taken(1 << k, bits1, bits2):
                    i1, j1 = p, k
                    res = max(res, dp(p + 1, bits1 | (1 << i1) | (1 << j1), bits2))
            i1, j1 = freeze[:2]

            for k in range(i2 + 1, j2):
                if s[k] == s[p] and not is_taken(1 << k, bits1, bits2):
                    i2, j2 = p, k
                    res = max(res, dp(p + 1, bits1, bits2 | (1 << i2) | (1 << j2)))
            i2, j2 = freeze[2:]

            # as the middle point
            if p < j1:
                i1 = j1 = p
                res = max(res, dp(p + 1, bits1 | mask, bits2))
                i1, j1 = freeze[:2]

            if p < j2:
                i2 = j2 = p
                res = max(res, dp(p + 1, bits1, bits2 | mask))
                i2, j2 = freeze[2:]

            return res

        return dp(0, 0, 0)

