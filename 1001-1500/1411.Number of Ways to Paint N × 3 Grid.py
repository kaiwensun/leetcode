cache = {}
class Solution:
    def numOfWays(self, n: int) -> int:
        def all_color():
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        if i != j != k:
                            yield (i, j, k)
        def can_be_adjacent(row1, row2):
            for i in range(3):
                if row1[i] == row2[i]:
                    return False
            return True
        def dfs(i, row_color):
            if (i, row_color) in cache:
                return cache[i, row_color]
            if i == 1:
                return 1
            res = 0
            for prev_row_color in all_color():
                if can_be_adjacent(row_color, prev_row_color):
                    res += dfs(i - 1, prev_row_color)
            cache[i, row_color] = res
            return res
        return sum(dfs(n, row_color) for row_color in all_color()) % (10 ** 9 + 7)
