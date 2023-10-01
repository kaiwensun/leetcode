class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_ks, min_ks = [nums[-1]], [nums[-1]]
        for k in range(len(nums) - 2, 1, -1):
            max_ks.append(max(nums[k], max_ks[-1]))
            min_ks.append(min(nums[k], max_ks[-1]))
        max_i = min_i = nums[0]
        res = 0
        for i in range(1, len(nums) - 1):
            max_k = max_ks.pop()
            min_k = min_ks.pop()
            for a in min_i, max_i:
                for c in max_k, min_k:
                    res = max(res, (a - nums[i]) * c)
            min_i = min(min_i, nums[i])
            max_i = max(max_i, nums[i])
        return res

