from itertools import chain
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        stack = []
        res = 0
        for c in chain(s, "#"):
            if c in "ab":
                if x < y:
                    c = "b" if c == "a" else "a"
                stack.append(c)
                if len(stack) >= 2 and stack[-2] == "a" and stack[-1] == "b":
                    stack.pop()
                    stack.pop()
                    res += max(x, y)
            elif stack:
                cnt = Counter(stack)
                res += min(x, y) * min(cnt["a"], cnt["b"])
                stack = []
        return res

