class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = len([x for x in nums if x == 1])
        N = len(nums)
        res = cur = 0
        l = -ones
        for r in range(-ones, N):
            if nums[r] == 1:
                cur += 1
            if r - l >= ones:
                if nums[l] == 1:
                    cur -= 1
                l += 1
            res = max(res, cur)
        return ones - res

