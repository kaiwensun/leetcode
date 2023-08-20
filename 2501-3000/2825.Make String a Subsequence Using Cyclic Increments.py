class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def match(c1, c2):
            return c1 == c2 or chr((ord(c1) + 1 - 97) % 26 + 97) == c2

        it1 = iter(str1)
        for c2 in str2:
            c1 = next(it1, None)
            while c1 is not None and not match(c1, c2):
                c1 = next(it1, None)
            if c1 is None:
                return False
        return True

