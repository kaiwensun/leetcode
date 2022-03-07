class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int: 
        res = 0
        nums.append(0)
        nums.sort()
        nums.append(float("inf"))
        for i in range(len(nums) - 1):
            start = nums[i] + 1
            end = nums[i + 1] - 1 if nums[i + 1] - nums[i] - 1 <= k else nums[i] + k
            if start > end:
                continue
            k -= nums[i + 1] - nums[i] - 1
            res += (start + end) * (end - start + 1) // 2
            if k <= 0:
                break
        return res

