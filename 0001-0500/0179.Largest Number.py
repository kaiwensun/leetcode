class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int("".join(sorted(map(str, nums), reverse=True, cmp=lambda str1, str2: cmp(str1 + str2, str2 + str1)))))
