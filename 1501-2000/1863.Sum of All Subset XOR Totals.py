from itertools import chain, combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xors = []
        for num in nums:
            xors.extend([num ^ xor for xor in xors])
            xors.append(num)
        return sum(xors)

