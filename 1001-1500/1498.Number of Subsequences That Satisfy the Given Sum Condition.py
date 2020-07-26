import collections, bisect
MOD = 10 ** 9 + 7
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        cnt = collections.Counter(nums)
        nums.sort()
        res = 0
        for index, num in enumerate(nums):
            if num + num > target: break
            rindex = bisect.bisect(nums, target - num, lo=index)
            size = rindex - index - 1
            res += (1 << size) % MOD
            res %= MOD
        return res % MOD
