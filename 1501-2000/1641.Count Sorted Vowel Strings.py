from functools import lru_cache
class Solution:
    @lru_cache(None)
    def countVowelStrings(self, n: int, charset=5) -> int:
        if charset == 1:
            return 1
        if n == 1:
            return charset
        return sum(self.countVowelStrings(n - 1, new_charset) for new_charset in range(1, charset + 1))

