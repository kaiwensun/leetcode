import itertools

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for comb in itertools.combinations(nums, 3):
            res = max(res, (comb[0] - comb[1]) * comb[2])
        return res

