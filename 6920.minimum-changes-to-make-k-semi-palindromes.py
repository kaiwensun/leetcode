from functools import cache

@cache
def get_factors(n):
    res = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            j = n // i
            res.append(i)
            if i != j:
                res.append(j)
    return res

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        @cache
        def countMinChangesToSemiPalindrome(start, end):
            res = float("inf")
            for factor in get_factors(end - start):
                sm = 0
                for shift in range(factor):
                    l = start + shift
                    r = end - factor + shift
                    while l < r:
                        if s[l] != s[r]:
                            sm += 1
                        l += factor
                        r -= factor
                res = min(res, sm)
                if res == 0:
                    break
            return res

        @cache
        def dp(start, k):
            if start == len(s):
                return 0 if k == 0 else float("inf")
            res = float("inf")
            for next_start in range(start + 2, len(s) + 1):
                res = min(res, countMinChangesToSemiPalindrome(start, next_start) + dp(next_start, k - 1))
            return res
        return dp(0, k)

