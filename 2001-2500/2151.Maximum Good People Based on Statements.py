from functools import cache

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:

        def validate_dp(i, good, bad):
            for j, statement in enumerate(statements[i]):
                if statement == 1 and ((1 << j) & bad):
                    return float("-inf")
                if statement == 0 and ((1 << j) & good):
                    return float("-inf")
                if statement == 1:
                    good |= 1 << j
                if statement == 0:
                    bad |= 1 << j
            return dp(i + 1, good, bad)

        @cache
        def dp(i, good, bad):
            if i == len(statements):
                return bin(good).count('1')
            mask = 1 << i
            if (mask & good):
                return validate_dp(i, good, bad)
            if (mask & bad):
                return dp(i + 1, good, bad)
            return max(dp(i + 1, good, bad | mask), validate_dp(i, good | mask, bad))

        return dp(0, 0, 0)

