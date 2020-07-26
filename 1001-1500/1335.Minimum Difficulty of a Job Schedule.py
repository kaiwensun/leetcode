from functools import lru_cache
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @lru_cache(None)
        def oneDayDifficulty(start, end):
            if start + 1 == end:
                return jobDifficulty[start]
            mid = (start + end) // 2
            return max(oneDayDifficulty(start, mid), oneDayDifficulty(mid, end))
        @lru_cache(None)
        def dp(nextTask, days):
            if days == 1:
                return oneDayDifficulty(0, nextTask)
            res = float("inf")
            for startTask in range(days - 1, nextTask):
                res = min(res, dp(startTask, days - 1) + oneDayDifficulty(startTask, nextTask))
            return res
        res = dp(len(jobDifficulty), d)
        return -1 if res == float('inf') else res
