from functools import cache

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_palindrome(start, size):
            if start + size > len(s):
                return False
            l = start
            r = start + size - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        lenk0 = [is_palindrome(i, k) for i in range(len(s))]
        lenk1 = [is_palindrome(i, k + 1) for i in range(len(s))]

        @cache
        def dp(i):
            if i + k > len(s):
                return 0
            res = dp(i + 1)
            if lenk0[i]:
                res = max(res, 1 + dp(i + k))
            if lenk1[i]:
                res = max(res, 1 + dp(i + k + 1))
            return res
        return dp(0)

