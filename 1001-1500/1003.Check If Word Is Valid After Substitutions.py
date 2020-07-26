class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for c in S:
            stack.append(c)
            if stack[-1] == "c":
                if len(stack) >= 3 and stack[-3] == "a" and stack[-2] == "b":
                    stack = stack[:-3]
                else:
                    return False
        return not stack
