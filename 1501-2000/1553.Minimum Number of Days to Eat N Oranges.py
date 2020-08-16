from collections import deque
class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        seen = set()
        queue = deque([(n, 1)])
        while queue:
            num, step = queue.popleft()
            nexts = [num - 1]
            if num % 2 == 0: nexts.append(num // 2)
            if num % 3 == 0: nexts.append(num // 3)
            for nxt in nexts:
                if nxt not in seen:
                    if nxt == 1:
                        return step + 1
                    seen.add(nxt)
                    queue.append((nxt, step + 1))

