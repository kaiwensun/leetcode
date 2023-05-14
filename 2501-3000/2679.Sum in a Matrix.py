class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        return sum(map(max, zip(*map(sorted, nums))))

