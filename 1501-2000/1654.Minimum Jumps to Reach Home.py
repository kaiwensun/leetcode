from collections import deque
class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        MAX = max(max(forbidden), x) + max(a, b) * 2
        forbidden = set(forbidden)
        visited = {(0, True)}
        queue = deque([(0, True), ("#", "#")])
        res = 0
        while len(queue) != 1:
            p, can_backward = queue.popleft()
            if p == "#":
                queue.append(("#", "#"))
                res += 1
                continue
            if p == x:
                return res
            if p + a <= MAX and p + a not in forbidden and (p + a, True) not in visited:
                visited.add((p + a, True))
                queue.append((p + a, True))
            if can_backward and p - b > 0 and p - b not in forbidden and (p - b, False) not in visited and (p - b, True) not in visited:
                visited.add((p - b, False))
                queue.append((p - b, False))
        return -1

