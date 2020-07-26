import functools
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(time, index):
            if index == len(satisfaction):
                return 0
            return max(
                time * satisfaction[index] + dp(time + 1, index + 1),
                dp(time, index + 1)
            )
        satisfaction.sort()
        return dp(1, 0)
