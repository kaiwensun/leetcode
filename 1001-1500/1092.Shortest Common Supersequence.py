class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        """
        return (subsequence length, instruction)
        instruction means:
            0: base case
            1: take i from str1
            2: take j from str2
            3: take i and j from str1 and str2
        """
        INF = len(str1) + len(str2) + 1

        @lru_cache(None)
        def dp(i, j):
            if i == j == -1:
                return 0, 0
            if j == -1:
                return i + 1, 1
            if i == -1:
                return j + 1, 2
            res = (INF, -1)
            if res[0] > dp(i - 1, j)[0] + 1:
                res = dp(i - 1, j)[0] + 1, 1
            if res[0] > dp(i, j - 1)[0] + 1:
                res = dp(i, j - 1)[0] + 1, 2
            if str1[i] == str2[j] and res[0] > dp(i - 1, j - 1)[0] + 1:
                res = dp(i - 1, j - 1)[0] + 1, 3
            return res

        def reconstruct(i, j):
            ins = dp(i, j)[1]
            if ins == 0:
                res = []
            elif ins == 1:
                res = reconstruct(i - 1, j)
                res.append(str1[i])
            elif ins == 2:
                res = reconstruct(i, j - 1)
                res.append(str2[j])
            elif ins == 3:
                res = reconstruct(i - 1, j - 1)
                assert(str1[i] == str2[j])
                res.append(str1[i])
            else:
                assert(False)
            return res

        return "".join(reconstruct(len(str1) - 1, len(str2) - 1))

