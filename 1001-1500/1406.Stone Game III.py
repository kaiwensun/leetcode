from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        sm = [stoneValue[-1]] * len(stoneValue)
        for i in range(len(stoneValue) - 2, -1, -1):
            sm[i] = sm[i + 1] + stoneValue[i]
        
        def getSumSuf(i):
            if i >= len(stoneValue):
                return 0
            return sm[i]
        def getValue(i):
            if i >= len(stoneValue):
                return 0
            return stoneValue[i]
        @lru_cache(None)
        def dp(i):
            # if I pick starting from i, what is the optimal value I can get?, and the sum(stoneValue[i:])
            if i >= len(stoneValue):
                return 0
            return max(
                getValue(i) + getSumSuf(i + 1) - dp(i + 1),
                getValue(i) + getValue(i + 1) + getSumSuf(i + 2) - dp(i + 2),
                getValue(i) + getValue(i + 1) + getValue(i + 2) + getSumSuf(i + 3) - dp(i + 3)
            )
        alice = dp(0)
        bob = sm[0] - alice
        if alice == bob:
            return "Tie"
        return "Alice" if alice > bob else "Bob"
