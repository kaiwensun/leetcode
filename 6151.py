class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = [int(c) for c in str(n)]
        ln = len(s)
        def dfs(i, is_ceil, used):
            if i == ln:
                return 1
            res = 0
            if is_ceil:
                available = set(range(s[i] + 1)) - set(s[:i])
                if used == 0:
                    available.remove(0)
                if s[i] in available:
                    res += dfs(i + 1, True, used + 1)
                    available.remove(s[i])
                size = len(available)
                res += size * dfs(i + 1, False, used + 1)
            else:
                if used == 0:
                    available_size = 9
                else:
                    available_size = 10 - used
                assert(available_size > 0)
                res = available_size * dfs(i + 1, False, used + 1)
            return res
        return dfs(0, True, 0) + sum(dfs(i, False, 0) for i in range(1, ln))

