import functools
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7        
        @functools.lru_cache(None)
        def dp(i, j):
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != "X"):
                return 0, 0, False
            if board[i][j] == "E":
                return 0, 1, True
            left = dp(i, j - 1)
            up = dp(i - 1, j)
            upleft = dp(i - 1, j - 1)
            steps = tuple(filter(lambda step: step[2], (left, up, upleft)))
            mx = max(tuple(map(lambda step: step[0], steps)) or [-1])
            mxsteps = tuple(filter(lambda step: step[0] == mx, steps))
            if board[i][j] == "S":
                return mx, sum(step[1] for step in mxsteps) % MOD, bool(mxsteps)
            return mx + int(board[i][j]), sum(step[1] for step in mxsteps) % MOD, bool(mxsteps)
        res = list(dp(len(board) - 1, len(board[0]) - 1))
        return res[:2] if res[2] else [0, 0]
