class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        data = [[0, float('inf'), float('inf')] for _ in range(n)] # [[heights, left_arms, right_arms], ...]
        res = 0
        for row in matrix:
            row = list(map(int, row))
            new_data = [[0] * 3 for _ in range(n)]
            
            # new heights
            for i in range(n):
                new_data[i][0] = row[i] * (data[i][0] + row[i])
            
            # new left arms
            left = 0
            for i in range(n):
                left = row[i] * (left + row[i])
                if i == 0:
                    new_data[i][1] = row[i]
                else:
                    if data[i][0] == 0:
                        new_data[i][1] = left
                    else:
                        new_data[i][1] = min(left, data[i][1])
            # new right arms
            right = 0
            for i in range(n - 1, -1, -1):
                right = row[i] * (right + row[i])
                if i == n - 1:
                    new_data[i][2] = row[i]
                else:
                    if data[i][0] == 0:
                        new_data[i][2] = right
                    else:
                        new_data[i][2] = min(right, data[i][2])
                res = max(res, new_data[i][0] * (new_data[i][1] + new_data[i][2] - 1))
            data = new_data
        return res
