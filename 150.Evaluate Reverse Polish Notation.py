class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        op = {
            '+': int.__add__,
            '-': int.__sub__,
            '*': int.__mul__,
            '/': lambda x, y: int(float(x) / y)
        }
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack.append(int(token))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(op[token](v1, v2))
        return stack[0]
