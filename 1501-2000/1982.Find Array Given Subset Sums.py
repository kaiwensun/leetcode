from collections import Counter

"""
M = min of absolute of nums = sorted(sums)[0] - sorted(sums)[1].
Phen use `M` to split `sums` into two groups: one is contributed by M, one is not contributed by M.
Pick the one that is not contributed by M. Repeat the above process.
Until we find the absolute of nums.
min(sums) must be contributed by all negative numbers. Use it to determine which in nums should be negative.
"""

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        mn = sums[0]
        absolute_res = []
        for _ in range(n):
            num = sums[1] - sums[0]
            absolute_res.append(num)
            cnt = Counter(sums)
            next_sums = []
            for sm in sums:
                if cnt[sm] == 0:
                    continue
                cnt[sm] -= 1
                cnt[sm + num] -= 1
                next_sums.append(sm)
            sums = next_sums

        @cache
        def dp(i, remain):
            if remain < 0:
                return False
            if remain == 0:
                return True
            if i == len(absolute_res):
                return False
            return dp(i + 1, remain - absolute_res[i]) or dp(i + 1, remain)
        remain = -mn
        negative_res = []
        i = 0
        while remain != 0:
            if dp(i + 1, remain - absolute_res[i]):
                negative_res.append(absolute_res[i])
                remain -= absolute_res[i]
            i += 1
        return list((Counter(absolute_res) - Counter(negative_res)).elements()) + [-num for num in negative_res]

