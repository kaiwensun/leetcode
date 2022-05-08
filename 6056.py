class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for c in "9876543210":
            if c * 3 in num:
                return c * 3
        return ""

