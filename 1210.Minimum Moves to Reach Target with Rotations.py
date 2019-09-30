class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_empty(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid):
                return grid[r][c] == 0
            return False
        inf = float('inf')
        if grid[0][0] or grid[0][1] or grid[-1][-1] or grid[-1][-2]:
            return -1
        n = len(grid)
        dp = [[None, None] for _ in grid]
        dp[0] = [0, 1] if grid[1][0] == grid[1][1] == 0 else [0, inf]
        for c in xrange(1, n - 1):
            dp[c][0] = inf if grid[0][c + 1] else dp[c - 1][0] + 1
            if grid[0][c] == grid[1][c] == 0:
                dp[c][1] = min(dp[c - 1][1], dp[c][0] if grid[1][c + 1] == 0 else inf) + 1
            else:
                dp[c][1] = inf
        prev = dp
        dp = [[None, None] for _ in grid]
        for r in xrange(1, n):
            if is_empty(r + 1, 0):
                dp[0][1] = prev[0][1] + 1
            else:
                dp[0][1] = inf
            if is_empty(r, 0) and is_empty(r, 1):
                dp[0][0] = prev[0][0] + 1
                if is_empty(r + 1, 1):
                    dp[0][0] = min(dp[0][0], dp[0][1] + 1)
            else:
                dp[0][0] = inf
            for c in xrange(1, n - 1):
                if is_empty(r, c):
                    dp[c][0] = min(dp[c - 1][0], prev[c][0]) + 1 if is_empty(r, c + 1) else inf
                    dp[c][1] = min(dp[c - 1][1], prev[c][1]) + 1 if is_empty(r + 1, c) else inf
                    if is_empty(r + 1, c + 1):
                        dp[c][0] = min(dp[c][0], dp[c][1] + 1) if is_empty(r, c + 1) else inf
                        dp[c][1] = min(dp[c][1], dp[c][0] + 1) if is_empty(r + 1, c) else inf
                else:
                    dp[c][0] = dp[c][1] = inf
            dp, prev = prev, dp
        return -1 if prev[n - 2][0] == inf else prev[n - 2][0]
