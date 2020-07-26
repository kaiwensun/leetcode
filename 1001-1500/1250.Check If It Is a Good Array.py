import fractions
class Solution(object):
    def isGoodArray(self, nums):
        return reduce(fractions.gcd, nums, nums[0]) == 1
