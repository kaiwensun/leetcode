from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        s1 = [ord(c) - ord('a') for c in s1]
        s2 = [ord(c) - ord('a') for c in s2]

        @lru_cache(None)
        def dp(i, j, size):
            if size == 1:
                return s1[i] == s2[j]
            mask1 = mask2 = mask3 = 0
            cnt1, cnt2, cnt3 = [[0] * 26 for _ in range(3)]
            for k in range(1, size):
                c1, c2, c3 = s1[i + k - 1], s2[j + k - 1], s2[j + size - k]
                mask1 ^= 1 << c1; mask2 ^= 1 << c2; mask3 ^= 1 << c3
                cnt1[c1] += 1; cnt2[c2] += 1; cnt3[c3] += 1
                if mask1 == mask2 and cnt1 == cnt2 and dp(i, j, k) and dp(i + k, j + k, size - k):
                    return True
                if mask1 == mask3 and cnt1 == cnt3 and dp(i, j + size - k, k) and dp(i + k, j, size - k):
                    return True
            return False
        return dp(0, 0, len(s1))

