class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        for num in nums:
            if num in seen:
                seen.discard(num)
            else:
                seen.add(num)
        return list(seen)

