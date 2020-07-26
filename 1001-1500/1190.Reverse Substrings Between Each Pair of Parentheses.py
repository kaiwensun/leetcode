class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cur = ''
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = ''
            elif c == ')':
                cur = stack.pop() + cur[::-1]
            else:
                cur += c
        return cur
