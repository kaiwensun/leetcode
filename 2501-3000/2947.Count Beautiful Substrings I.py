class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        res = 0
        for i in range(len(s)):
            v_cnt = 0
            for j in range(i, len(s)):
                if s[j] in vowels:
                    v_cnt += 1
                c_cnt = j - i + 1 - v_cnt
                if c_cnt == v_cnt and (c_cnt * v_cnt) % k == 0:
                    res += 1
        return res

