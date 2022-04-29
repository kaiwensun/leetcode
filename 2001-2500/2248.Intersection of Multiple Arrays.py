class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for s in map(set, nums[1:]):
            res &= s
        return sorted(res)

