class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        res = sum(nums)
        for shift in range(1, len(nums)):
            head = nums[0]
            for i in range(len(nums) - 1):
                nums[i] = min(nums[i], nums[i + 1])
            nums[-1] = min(nums[-1], head)
            res = min(res, sum(nums) + x * shift)
        return res

