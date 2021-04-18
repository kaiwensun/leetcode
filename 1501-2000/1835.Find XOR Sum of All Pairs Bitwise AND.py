class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        WIDTH = len(bin(10 ** 9)) - 2
        for shift in range(WIDTH):
            mask = 1 << shift
            ones1 = sum(num & mask == mask for num in arr1)
            ones2 = sum(num & mask == mask for num in arr2)
            res |= (ones1 & ones2 & 1) << shift
        return res

