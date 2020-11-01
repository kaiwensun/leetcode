from functools import lru_cache
from collections import Counter

MOD = 10 ** 9 + 7

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        @lru_cache(None)
        def dp(i, k):            
            if i == len(target):
                return 1
            if k == len(index2chars):
                return 0
            res = dp(i, k + 1)
            if target[i] in index2chars[k]:
                res += index2chars[k][target[i]] * dp(i + 1, k + 1)
            return res % MOD
        
        index2chars = [Counter(chars) for chars in zip(*words)]
        return dp(0, 0)

