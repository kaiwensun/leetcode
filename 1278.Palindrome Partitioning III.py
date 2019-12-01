import functools
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        
        @functools.lru_cache(None)
        def numOfReplacementNeeded(i, j):
            res = 0
            while i < j:
                res += s[i] != s[j]
                i += 1
                j -= 1
            return res
        
        # how many replacements are needed
        @functools.lru_cache(None)
        def dp(end, numOfPalindrome):
            assert(0 < numOfPalindrome <= end)
            p = numOfPalindrome
            if end == p:
                return 0
            if end == 1:
                return 0
            if p == 1:
                return numOfReplacementNeeded(0, end - 1)
            return min(dp(end - i, p - 1) + numOfReplacementNeeded(end - i, end - 1) for i in range(1, end - p + 2))
        return dp(len(s), k)
