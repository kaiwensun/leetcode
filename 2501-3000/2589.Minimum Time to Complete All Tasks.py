"""
Idea:

Imagine each task is a tile of length `duration`. The tile can freely slide in the range of [start, end].
Initially all tiles are at their most-left possible position.
We use a screen to push tiles rightward, until at least one tile touched by the screen cannot be pushed more rightward, because it is bounded by `end`. Find out the biggest of such `end`.
Now we run all applicable tasks in the time range from the screen's position to the biggest `end`.
"""

class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:

        class Tile:
            def __init__(self, task):
                self.start, self.end, self.duration = task

            def can_push_right(self, t):
                return t + self.duration <= self.end

            def is_touched(self, t):
                return t >= self.start

            def is_complete(self):
                return self.duration <= 0

            def run_in_range(self, start, end):
                if self.is_complete():
                    return
                start = max(self.start, start)
                end = min(self.end, end)
                duration = max(0, end - start + 1)
                self.duration -= duration

            def __repr__(self):
                return str([self.start, self.end, self.duration])

        tasks.sort()
        MX_END = max(task[1] for task in tasks)
        MN_START = tasks[0][0]


        tiles = [Tile(task) for task in tasks]
        total_duration = 0
        t = MN_START
        while t <= MX_END:
            touched_tiles = []
            for tile in tiles:
                if not tile.is_touched(t):
                    break
                if not tile.is_complete():
                    touched_tiles.append(tile)
            else:
                if not touched_tiles:
                    break

            end = 0
            for tile in touched_tiles:
                if not tile.can_push_right(t):
                    end = max(end, tile.end)
            if end:
                for tile in tiles:
                    tile.run_in_range(t, end)
                duration = end - t + 1
                total_duration += duration
                t = end
            t += 1
        return total_duration

