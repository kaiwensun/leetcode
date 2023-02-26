import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        def get_neighbors(cell):
            DELTA = [-1, 0, 1, 0, -1]
            for k in range(4):
                x = cell[1] + DELTA[k]
                y = cell[2] + DELTA[k + 1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    yield (grid[x][y], x, y)

        M, N = len(grid), len(grid[0])
        if M == N == 1:
            return 0
        if all(neighbor[0] > 1 for neighbor in get_neighbors((0, 0, 0))):
            return -1
        seen = set()
        queues = [[(0, 0, 0)], []] # [[[value, i, j], ...], []]
        cur_time = 1
        to_revives = [[], []]
        while True:
            from_queue, to_queue = queues
            while to_revives[0] and to_revives[0][0][0] <= cur_time:
                item = heapq.heappop(to_revives[0])
                heapq.heappush(from_queue, item[1])

            while from_queue and from_queue[0][0] < cur_time:
                cell = heapq.heappop(from_queue)
                seen.add(cell)
                revive_at = float("inf")
                for neighbor in get_neighbors(cell):
                    if neighbor[0] > cur_time:
                        revive_at = min(revive_at, neighbor[0])
                        continue
                    if neighbor[1] == M - 1 and neighbor[2] == N - 1:
                        return cur_time
                    if neighbor not in seen:
                        seen.add(neighbor)
                        heapq.heappush(to_queue, neighbor)
                if revive_at != float("inf"):
                    heapq.heappush(to_revives[0], (revive_at, cell))
            cur_time += 1
            queues.reverse()
            to_revives.reverse()

