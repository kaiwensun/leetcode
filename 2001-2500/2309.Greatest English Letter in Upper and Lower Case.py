class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for A, a in reversed(list(zip(string.ascii_uppercase, string.ascii_lowercase))):
            if a in s and A in s:
                return A
        return ""

