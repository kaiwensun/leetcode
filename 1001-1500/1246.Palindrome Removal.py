# see another memoization solution

class Solution(object):
    def minimumMoves(self, arr):
        dp = [[]]
        for length in range(0, len(arr) + 1):
            dp.append([])
            for start in range(0, len(arr) - length + 1):
                if length <= 1:
                    res = 1
                else:
                    if arr[start] == arr[start + length - 1]:
                        res = dp[length - 2][start + 1]
                    else:
                        res = min(dp[first_length][start] + dp[length - first_length][start + first_length] for first_length in range(1, length))
                dp[length].append(res)
        return dp[len(arr)][0]
