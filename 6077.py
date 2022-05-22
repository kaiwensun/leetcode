from functools import cache

MOD = 10 ** 9 + 7

class Solution:
    def totalStrength(self, strength: List[int]) -> int:

        N = len(strength)

        @cache
        def prefix_sum(i):
            if i == -1:
                return 0
            return (strength[i] + prefix_sum(i - 1)) % MOD

        def suffix_sum(i):
            return (prefix_sum(N - 1) - prefix_sum(i - 1)) % MOD

        @cache
        def prefix_sum_of_prefix_sum(i):
            if i == -1:
                return 0
            return (prefix_sum(i) + prefix_sum_of_prefix_sum(i - 1)) % MOD

        @cache
        def suffix_sum_of_suffix_sum(i):
            if i == N:
                return 0
            return (suffix_sum(i) + suffix_sum_of_suffix_sum(i + 1)) % MOD

        def range_sum_of_prefix_sum(start, end):
            if start > end: return 0
            return (prefix_sum_of_prefix_sum(end) - prefix_sum_of_prefix_sum(start - 1) - prefix_sum(start - 1) * (end - start + 1)) % MOD

        def range_sum_of_suffix_sum(start, end):
            if start > end: return 0
            return (suffix_sum_of_suffix_sum(start) - suffix_sum_of_suffix_sum(end + 1) - suffix_sum(end + 1) * (end - start + 1)) % MOD

        def calc(i):
            l, r = leftBorder[i], rightBorder[i]
            return (range_sum_of_suffix_sum(l, i) * (r - i + 1) + range_sum_of_prefix_sum(i + 1, r) * (i - l + 1)) % MOD

        def get_range_sum(start, end):
            return prefix_sum[end] - prefix_sum[start]

        def getLeftBorderIndex(arr):
            arr.append(float("-inf"))
            stack = [-1]
            res = []
            for i in range(N):
                while arr[stack[-1]] >= arr[i]:
                    stack.pop()
                res.append(stack[-1] + 1)
                stack.append(i)
            arr.pop()
            return res

        def getRightBorderIndex(arr):
            arr.append(float("-inf"))
            stack = [N]
            res = [None] * N
            for i in range(N - 1, -1, -1):
                while arr[stack[-1]] > arr[i]:
                    stack.pop()
                res[i] = stack[-1] - 1
                stack.append(i)
            arr.pop()
            return res

        leftBorder = getLeftBorderIndex(strength)
        rightBorder = getRightBorderIndex(strength)
        res = 0
        for i in range(N):
            res += calc(i) * strength[i]
            res %= MOD
        return res

