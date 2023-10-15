class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mn, mn_ind = float("inf"), None
        mx, mx_id = float("-inf"), None
        for i, num in enumerate(nums):
            if mn > num:
                mn = num
                mn_ind = i
            if mx < num:
                mx = num
                mx_ind = i
            j = i + indexDifference
            if j >= len(nums):
                break
            if nums[j] - mn >= valueDifference:
                return mn_ind, j
            if mx - nums[j] >= valueDifference:
                return mx_ind, j
        return -1, -1

