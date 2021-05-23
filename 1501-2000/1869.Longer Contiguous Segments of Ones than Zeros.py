class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = max(len(word) for word in s.split("0"))
        zeros = max(len(word) for word in s.split("1"))
        return ones > zeros

