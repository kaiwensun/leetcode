from collections import deque, defaultdict

class Solution(object):
    def minimumVisitedCells(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        if M == N == 1:
            return 1
        steps = [[None] * N for _ in xrange(M)]
        visited = set()
        split = ("#", "#")
        target = (M - 1, N - 1)
        queue = deque([(0, 0), split])
        res = 1
        row_max_reached = defaultdict(int)
        col_max_reached = defaultdict(int)
        while len(queue) > 1:
            i, j = queue.popleft()
            if i == "#":
                res += 1
                queue.append(split)
                continue
            start = min(N - 1, j + grid[i][j])
            for dj in xrange(start, max(row_max_reached[i], j), -1):
                nxt = (i, dj)
                if nxt in visited:
                    continue
                if nxt == target:
                    return res + 1
                visited.add(nxt)
                queue.append(nxt)
                if j <= row_max_reached[i]:
                    row_max_reached[i] = j
            start = min(M - 1, i + grid[i][j])
            for di in xrange(start, max(col_max_reached[j], i), -1):
                nxt = (di, j)
                if nxt in visited:
                    continue
                if nxt == target:
                    return res + 1
                visited.add(nxt)
                queue.append(nxt)
                if i <= row_max_reached[j]:
                    row_max_reached[j] = i
        return -1

