class Solution(object):
    def minTaps(self, n, ranges):
        ranges = sorted([(i - r, min(i + r, n)) for i, r in enumerate(ranges)])
        stack = [(0, 0), (0, 0)]
        for r in ranges:
            if r[0] > stack[-1][1]:
                break
            if r[1] <= stack[-1][1]:
                continue
            while r[0] <= stack[-2][1] and len(stack) > 2:
                stack.pop()
            stack.append(r)
        if stack[-1][1] == n:
            return len(stack) - 2
        else:
            return -1
