from functools import cache


bitmap2id = {1 << i : i for i in range(14)}

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:

        def iter_bitmap(bitmap):
            while bitmap:
                bit = bitmap ^ ((bitmap - 1) & bitmap)
                yield bit
                bitmap ^= bit

        @cache
        def dp(todos, remain):
            if todos == 0:
                return 0
            res = float("inf")
            for todo in iter_bitmap(todos):
                task = tasks[bitmap2id[todo]]
                if remain >= task:
                    res = min(res, dp(todos ^ todo, remain - task))
            if res == float("inf"):
                res = 1 + dp(todos, sessionTime)
            return res

        return dp((1 << len(tasks)) - 1, sessionTime) + 1

