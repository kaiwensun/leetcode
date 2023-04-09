from functools import cache

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        @cache
        def dp(i, j):
            if i == M - 1 and j == N - 1:
                return 1
            if grid[i][j] == 0:
                return float("inf")
            res = 1 + min(
                row_seg_trees[i].get_min(min(N, j + 1), min(N, j + grid[i][j] + 1)),
                col_seg_trees[j].get_min(min(M, i + 1), min(M, i + grid[i][j] + 1))
            )
            return res

        class SegmentTree:
            def __init__(self, size):
                self.size = size
                self.arr = [float("inf")] * (size * 2)

            def put(self, i, num):
                i += self.size
                self.arr[i] = num
                while i > 0:
                    j = i // 2
                    self.arr[j] = min(self.arr[j * 2], self.arr[j * 2 + 1])
                    i = j

            def get_min(self, left, right):
                orig_l, orig_r = left, right
                left += self.size
                right += self.size
                res = float("inf")
                while left < right:
                    if left % 2:
                        res = min(res, self.arr[left])
                        left += 1
                    if right % 2:
                        right -= 1
                        res = min(res, self.arr[right])
                    left //= 2
                    right //= 2
                return res

        row_seg_trees = [SegmentTree(N) for _ in range(M)]
        col_seg_trees = [SegmentTree(M) for _ in range(N)]
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                res = dp(i, j)
                row_seg_trees[i].put(j, res)
                col_seg_trees[j].put(i, res)
        res = dp(0, 0)
        dp.cache_clear()
        return -1 if res == float("inf") else res

