class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1:
            return -1 if k % 2 == 1 else nums[0]
        if len(nums) == 2:
            return nums[k % 2] if k <= 2 else max(nums)
        return max(nums[:k - 1] + nums[k: k + 1])

