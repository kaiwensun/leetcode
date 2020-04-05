class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda a, b : a ^ b, nums)
