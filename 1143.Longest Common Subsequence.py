class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        print text1, text2
        M, N = len(text1), len(text2)
        dp_common_ended_at = [[0] * N, [0] * N]
        dp_common_range_mx = [[0] * N, [0] * N]
        for m in xrange(M):
            for n in xrange(N):
                if text1[m] == text2[n]:
                    dp_common_ended_at[1][n] = max(
                        n and dp_common_range_mx[1][n - 1],
                        m and dp_common_range_mx[0][n],
                        (m and n and dp_common_range_mx[0][n - 1]) + 1
                    )
                dp_common_range_mx[1][n] = max(
                    m and dp_common_range_mx[0][n],
                    n and dp_common_range_mx[1][n - 1],
                    dp_common_ended_at[1][n]
                )
            dp_common_ended_at[0][:] = [0] * N
            dp_common_ended_at[0], dp_common_ended_at[1] = dp_common_ended_at[1], dp_common_ended_at[0]
            dp_common_range_mx[0][:] = [0] * N
            dp_common_range_mx[0], dp_common_range_mx[1] = dp_common_range_mx[1], dp_common_range_mx[0]
        return dp_common_range_mx[0][-1]
