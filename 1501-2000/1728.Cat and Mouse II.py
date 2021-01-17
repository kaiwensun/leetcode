class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        M, N = len(grid), len(grid[0])
        def can_go(i, j):
            return 0 <= i < M and 0 <= j < N and grid[i][j] != "#"
        DELTA = (1, 0, -1, 0, 1)
        MAX_TURN = sum(row.count(".") for row in grid) + 2

        def check(mi, mj, ci, cj, turns):
            if mi == ci and mj == cj:
                return False
            if turns == MAX_TURN * 2:
                return False
            if grid[mi][mj] == "F":
                return True
            if grid[ci][cj] == "F":
                return False
            return None

        @lru_cache(None)
        def dp(mi, mj, ci, cj, turns):
            expect = turns & 1 == 0
            mx, my, cx, cy = mi, mj, ci, cj
            jump = mouseJump if expect else catJump
            for k in range(4):
                dx, dy = DELTA[k], DELTA[k + 1]
                for step in range(jump + 1):
                    if expect:
                        mx, my = mi + dx * step, mj + dy * step
                        if not can_go(mx, my):
                            break
                    else:
                        cx, cy = ci + dx * step, cj + dy * step
                        if not can_go(cx, cy):
                            break
                    res = check(mx, my, cx, cy, turns + 1)
                    if res is None:
                        res = dp(mx, my, cx, cy, turns + 1)
                    if expect == res:
                        return expect
            return not expect

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "C":
                    ci, cj = i, j
                elif grid[i][j] == "M":
                    mi, mj = i, j
        return dp(mi, mj, ci, cj, 0)

