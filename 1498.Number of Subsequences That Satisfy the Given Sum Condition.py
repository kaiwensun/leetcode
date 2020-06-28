import collections, bisect
MOD = 10 ** 9 + 7
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        cnt = collections.Counter(nums)
        nums.sort()
        res = 0
        for index, num in enumerate(nums):
            rindex = bisect.bisect(nums, target - num, lo=index)
            size = rindex - index - 2
            if size >= 0:
                res += ((1 << (size + 1)) - 1) % MOD
                res %= MOD
            if num + num <= target:
                res += 1
        return res % MOD
