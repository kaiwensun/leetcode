import functools, collections, bisect, string

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        c2i = collections.defaultdict(list)
        word = word1 + word2
        for c in string.ascii_lowercase:
            c2i[c].append(-1)
        for i, c in enumerate(word):
            c2i[c].append(i)
        for c in string.ascii_lowercase:
            c2i[c].append(len(word))

        @functools.lru_cache(None)
        def dp(i, j, matched):
            if i > j:
                return 0
            if not matched and (i >= len(word1) or j < len(word1)):
                return 0
            if i == j:
                return 1
            if word[i] == word[j]:
                return 2 + dp(i + 1, j - 1, True)
            res = int(matched)
            res = max(res, dp(i + 1, j - 1, matched))
            c1, c2 = word[i], word[j]
            next_i = c2i[c2][bisect.bisect_left(c2i[c2], i + 1)]
            next_j = c2i[c1][bisect.bisect_left(c2i[c1], j) - 1]
            res = max(res, dp(next_i, j, matched))
            res = max(res, dp(i, next_j, matched))
            return res
        return dp(0, len(word) - 1, False)

