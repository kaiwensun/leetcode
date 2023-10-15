class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        array = []
        for row in grid:
            array.extend(row)
        size = len(array)
        left = [1]
        for num in array[:-1]:
            left.append(left[-1] * num % MOD)

        right = [1]
        for num in array[-1:0:-1]:
            right.append(right[-1] * num % MOD)
        right.reverse()
        res = [l * r  % MOD for l, r in zip(left, right)]
        return [
            res[i : i + len(grid[0])] for i in range(0, size, len(grid[0]))
        ]

