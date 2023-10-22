class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = float("inf")
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[j] <= nums[k]:
                        continue
                    res = min(res, nums[i] + nums[j] + nums[k])
        return -1 if res == float("inf") else res

