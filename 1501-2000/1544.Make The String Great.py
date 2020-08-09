class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        delta = ord('a') - ord('A')
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and abs(ord(stack[-1]) - ord(stack[-2])) == delta:
                stack.pop()
                stack.pop()
        return "".join(stack)
