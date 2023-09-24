from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = Counter(s)
        return "1" * (c["1"] - 1) + "0" * c["0"] + "1"

