from functools import lru_cache

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
        # redefine flags
        #  3: mouse wins
        #  4: draw
        #  5: cat wins
        @lru_cache(None)
        def dp(step, mouse, cat):
            if mouse == 0 or cat == 0:
                return 3
            if mouse == cat:
                return 5
            if step == 2 * len(graph):
                return 4
            if step % 2:  # cat moves
                res = 3
                for nxt in graph[cat]:
                    res = max(res, dp(step + 1, mouse, nxt))
                    if res == 5:
                        break
            else:  # mouse moves
                res = 5
                for nxt in graph[mouse]:
                    res = min(res, dp(step + 1, nxt, cat))
                    if res == 3:
                        break
            return res

        res = dp(0, 1, 2)
        if res == 3: return 1
        if res == 4: return 0
        if res == 5: return 2

