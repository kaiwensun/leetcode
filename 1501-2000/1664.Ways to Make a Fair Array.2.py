class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        l = [0, 0]
        r = [sum(nums[0::2]), sum(nums[1::2])]
        res = 0
        for i, num in enumerate(nums):
            r[i % 2] -= num
            res += int(l[1] + r[0] == l[0] + r[1])
            l[i % 2] += num
        return res

