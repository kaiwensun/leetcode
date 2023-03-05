from functools import cache

class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        types.sort(key=lambda t: t[1])
        MOD = 10 ** 9 + 7

        @cache
        def dp(type_id, remain_marks):
            if type_id == len(types):
                return 1 if remain_marks == 0 else 0
            count, marks = types[type_id]
            res = dp(type_id + 1, remain_marks)
            for i in range(count):
                remain_marks -= marks
                if remain_marks < 0:
                    break
                res += dp(type_id + 1, remain_marks)
                res %= MOD
            return res
        return dp(0, target)

