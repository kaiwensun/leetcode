class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        i_grid = sorted(enumerate(grid), key=lambda item: sum(item[1]), reverse=True)
        @cache
        def dp(i, rows_cnt, acc):
            if rows_cnt and rows_cnt // 2 >= max(acc):
                return []
            if i == len(grid):
                return None
            res = dp(i + 1, rows_cnt, acc)
            if res is not None:
                return res
            if sum(i_grid[i][1]) == len(i_grid[i][1]):
                return None
            acc = tuple(map(sum, zip(acc, i_grid[i][1])))
            res = dp(i + 1, rows_cnt + 1, acc)
            if res is not None:
                res.append(i_grid[i][0])
                return res
            return None
        res = dp(0, 0, (0,) * len(grid[0]))
        return sorted(res) if res else []

