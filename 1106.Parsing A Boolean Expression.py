class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []
        for c in expression:
            if c != ',':
                if c == 't':
                    stack.append(True)
                elif c == 'f':
                    stack.append(False)
                else:
                    stack.append(c)
            if stack[-1] == ')':
                stack.pop()
                and_, or_ = True, False
                while stack[-1] != '(':
                    b = stack.pop()
                    and_ = and_ and b
                    or_ = or_ or b
                stack.pop()
                if stack:
                    op = stack.pop()
                    if op == '&':
                        stack.append(and_)
                    elif op == '|':
                        stack.append(or_)
                    elif op == '!':
                        stack.append(not and_)
                    else:
                        assert(False)
        assert(len(stack) == 1)
        return stack[0]
