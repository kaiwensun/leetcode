class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        if n == 0:
            return True
        for i, row in enumerate(mat):
            for j in range(len(row)):
                # odd or even index doesn't matter!
                if row[j] != row[(j + k) % n]:
                    return False
        return True

