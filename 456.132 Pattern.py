class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = [] # (num, min_so_far)
        mn = float('inf')
        for num in nums:
            mn = min(mn, num)
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append((num, mn))
        return False
