import functools
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mx_w = sum(stones)
        @functools.lru_cache(None)
        def dp(i, diff):
            if i == 0:
                return diff == stones[0]
            me = stones[i]
            return dp(i - 1, abs(abs(diff - me))) or dp(i - 1, diff + me)

        for possible_diff in range(mx_w + 1):
            if dp(len(stones) - 1, possible_diff):
                return possible_diff
        assert(0)
