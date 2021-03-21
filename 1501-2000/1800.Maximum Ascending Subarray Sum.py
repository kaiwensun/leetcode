class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = sm = 0
        nums.append(-1)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i - 1]:
                sm += nums[i]
            else:
                sm = nums[i]
            res = max(res, sm)
        return res

