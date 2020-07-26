class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        for n in reversed(nums):
            while stack and stack[-1] <= n:
                stack.pop()
            stack.append(n)
        rval = []
        for n in reversed(nums):
            while stack and stack[-1] <= n:
                stack.pop()
            rval.append(stack[-1] if stack else -1)
            stack.append(n)
        return list(reversed(rval))
