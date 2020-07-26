import functools
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7        
        @functools.lru_cache(None)
        def dp(i, j):
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != "X"):
                return 0, 0
            if board[i][j] == "E":
                return 0, 1
            left = dp(i, j - 1)
            up = dp(i - 1, j)
            upleft = dp(i - 1, j - 1)
            steps = (left, up, upleft)
            mx = max(tuple(map(lambda step: step[0], steps)) or [-1])
            mxsteps = tuple(filter(lambda step: step[0] == mx, steps))
            s = sum(step[1] for step in mxsteps)
            cur = 0 if board[i][j] == "S" or s == 0 else int(board[i][j])
            return mx + cur, sum(step[1] for step in mxsteps) % MOD
        return list(dp(len(board) - 1, len(board[0]) - 1))
