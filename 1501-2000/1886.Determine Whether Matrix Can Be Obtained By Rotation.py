class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        target = tuple(map(tuple, target))
        for i in range(4):
            if (mat := tuple(zip(*reversed(mat)))) == target:
                return True
        return False

