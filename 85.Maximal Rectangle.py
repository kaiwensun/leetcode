class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def solveOneRow(skyline):
            stack = [[0, -1, -1]] # [[height, left_index, right_index], ...]
            res = 0
            for i, height in enumerate(skyline + [0]):
                while len(stack) > 1 and stack[-1][0] >= height:
                    top = stack.pop()
                    res = max(res, top[0] * (top[2] - stack[-1][1]))
                    stack[-1][2] = top[2]
                stack.append([height, i, i])
            return res
        
        if matrix:
            skyline = [0] * len(matrix[0])
        res = 0
        for row in matrix:
            skyline = map(lambda (r, s): int(r) * (int(r) + s), zip(row, skyline))
            res = max(res, solveOneRow(skyline))
        return res
