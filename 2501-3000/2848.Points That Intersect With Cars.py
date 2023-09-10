class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        res = 0
        i = 0
        while i < len(nums):
            start, end = nums[i]
            i += 1
            while i < len(nums) and nums[i][0] <= end:
                end = max(end, nums[i][1])
                i += 1
            res += end - start + 1
        return res

