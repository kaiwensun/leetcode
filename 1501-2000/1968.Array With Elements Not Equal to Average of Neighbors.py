class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i, j = 0, len(nums) - 1
        while i <= j:
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j -= 1
        if len(res) != len(nums):
            res.pop()
        return res

