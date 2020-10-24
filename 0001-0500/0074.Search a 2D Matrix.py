class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def get(i):
            return matrix[i // len(matrix[0])][i % len(matrix[0])]
        l, r = 0, len(matrix) * (len(matrix) and len(matrix[0]))
        while l < r - 1:
            mid = (l + r) // 2
            if get(mid) > target:
                r = mid
            else:
                l = mid
        return matrix and matrix[0] and get(l) == target

