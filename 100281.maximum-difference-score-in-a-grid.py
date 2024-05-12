class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        mns = [float("inf")] * len(grid[0])
        res = float("-inf")
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                mn = min(mns[j], mns[j - 1] if j else float("inf"))
                res = max(res, val - mn)
                mns[j] = min(mn, val)
        return res

