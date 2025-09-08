class Solution:
    def minOperations(self, s: str) -> int:
        mn = min((c for c in s if c != "a"), default="{")
        return ord("{") - ord(mn)

