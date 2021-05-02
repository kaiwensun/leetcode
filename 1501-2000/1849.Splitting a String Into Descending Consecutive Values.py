from functools import lru_cache

class Solution:
    def splitString(self, s: str) -> bool:
        @lru_cache(None)
        def dp(i, expected):
            if i == len(s):
                return True
            if expected == 0:
                return int(s[i:]) == 0
            if s[i] == "0":
                return i != len(s) - 1 and dp(i + 1, expected)
            expected_str = str(expected)
            expected_len = len(expected_str)
            return s[i: i + expected_len] == expected_str and dp(i + expected_len, expected - 1)
        if set(s) == {"0"}:
            return False
        for end in range(1, len(s)):
            if dp(0, int(s[:end])):
                return True
        return False


