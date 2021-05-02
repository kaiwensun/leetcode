class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = float("inf")
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(res, abs(i - start))
        return res

