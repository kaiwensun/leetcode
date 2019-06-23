class Solution(object):
    def braceExpansionII(self, exp):
        stack = []
        for c in exp:
            if c == '{':
                stack.append('{')
            elif c == '}':
                while stack[-2] == ',':
                    set2 = stack.pop()
                    stack.pop()
                    stack[-1].update(set2)
                assert(stack[-2] == '{')
                tail = stack.pop()
                stack[-1] = tail
            elif c == ',':
                stack.append(',')
            else:
                stack.append(set(c))
            while len(stack) > 1 and isinstance(stack[-1], set) and isinstance(stack[-2], set):
                set2 = stack.pop()
                set1 = stack.pop()
                stack.append(set(w1 + w2 for w1 in set1 for w2 in set2))
        assert(len(stack) == 1)
        return list(sorted(stack[-1]))
