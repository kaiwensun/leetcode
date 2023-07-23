class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        while nums:
            while len(nums) > 1 and nums[-2] <= nums[-1]:
                tail = nums.pop()
                nums[-1] += tail
            res = max(res, nums.pop())
        return res

