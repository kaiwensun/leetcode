class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        xor = reduce(int.__rxor__, nums)
        res = []
        mask = (1 << maximumBit) - 1
        for num in reversed(nums):
            res.append(~(xor & mask) & mask)
            xor ^= num
        return res

