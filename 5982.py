from functools import cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            points, brainpower = questions[i]
            return max(
                points + dp(i + brainpower + 1),
                dp(i + 1)
            )
        return dp(0)

