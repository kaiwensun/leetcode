from functools import reduce

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        bitmap = lambda row: reduce(lambda b, i_num: b | (i_num[1] << i_num[0]), enumerate(row), 0)
        seen = {}
        res = []
        for i, row in enumerate(grid):
            b = bitmap(row)
            if b == 0:
                return [i]
            if b in seen:
                continue
            for prev, j in seen.items():
                if prev & b == 0:
                    return [j, i]
            seen[b] = i
        return []

