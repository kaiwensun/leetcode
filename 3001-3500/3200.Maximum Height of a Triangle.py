class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        res = 0
        arrs = [[red, blue], [blue, red]]
        for start in 0, 1:
            arr = arrs[start]
            line = 1
            for line in range(1, 100):
                if arr[line % 2] < line:
                    break
                arr[line % 2] -= line
                res = max(res, line)
        return res

