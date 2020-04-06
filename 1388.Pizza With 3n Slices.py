import functools
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
        @functools.lru_cache(None)
        def dp(start, end, taken_count):
            if taken_count == len(slices) / 3:
                return 0
            if end - start + 1 < (len(slices) / 3 - taken_count) * 2 - 1:
                return float("-inf")
            return max(dp(start, end - 2, taken_count + 1) + slices[end], dp(start, end - 1, taken_count))
        return max(dp(0, len(slices) - 2, 0), dp(1, len(slices) - 1, 0))
