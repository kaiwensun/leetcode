import functools
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        @functools.lru_cache(None)
        def dp(i, j, preferBig):
            if i + 1 == j:
                return nums[i], str(nums[i])
            res = float('-inf') if preferBig else float('inf')
            prefer = max if preferBig else min
            bestSplit = None
            for split in range(i + 1, j):
                left = dp(i, split, preferBig)
                right = dp(split, j, not preferBig)
                if not right[0]:
                    continue
                quotient = left[0] / right[0]
                if prefer(quotient, res) != res:
                    res = quotient
                    bestSplit = split
            left = dp(i, bestSplit, preferBig)
            right = dp(bestSplit, j, not preferBig)
            formater = "%s/%s" if bestSplit + 1 == j else "%s/(%s)"
            return res, formater % (left[1], right[1])
        return dp(0, len(nums), max)[1]
        
            
