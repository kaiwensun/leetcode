class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        def isValid(matrix):
            for row in matrix:
                if sorted(row) != list(range(1, len(row) + 1)):
                    return False
            return True
        return isValid(matrix) and isValid(zip(*matrix))

