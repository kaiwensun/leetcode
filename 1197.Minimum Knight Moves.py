# There is also an O(1) solution if you can find the law
class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y == 0:
            return 0
        x, y = abs(x), abs(y)
        x, y = max(x, y), min(x, y)
        visited = {(0, 0): 0}
        queue = collections.deque(((0, 0),))
        while queue:
            curr = queue.popleft()
            curr_step = visited[curr]
            for delta in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)):
                neighbor = (curr[0] + delta[0], curr[1] + delta[1])
                if -3 < neighbor[0] < x + 3 and -3 < neighbor[1] < y + 3 and neighbor[1] - neighbor[0] < 3 and neighbor not in visited:
                    if neighbor == (x, y):
                        return curr_step + 1
                    visited[neighbor] = curr_step + 1
                    queue.append(neighbor)
        assert(0)
