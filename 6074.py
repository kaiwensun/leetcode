class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return len([c for c in s if c == letter]) * 100 // len(s)

