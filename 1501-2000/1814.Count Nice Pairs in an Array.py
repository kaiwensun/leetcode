from collections import Counter
class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reverser = lambda num : int("".join(reversed(str(num))))
        diff = [num - reverser(num) for num in nums]
        return sum((cnt - 1) * cnt // 2 for cnt in Counter(diff).values()) % (10 ** 9 + 7)

