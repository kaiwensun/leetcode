import functools
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @functools.lru_cache(None)
        def dp(start, end):
            if start + 1 == end:
                return 0, arr[start]
                # return summation, maximum
            summation = float('inf')
            for split_start in range(start + 1, end):
                left = dp(start, split_start)
                right = dp(split_start, end)
                summation = min(summation, left[0] + right[0] + left[1] * right[1])
            return summation, max(left[1], right[1])
        return dp(0, len(arr))[0]
