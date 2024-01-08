class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max(map(lambda d: (d[0] * d[0] + d[1] * d[1], d[0] * d[1]), dimensions))[1]

