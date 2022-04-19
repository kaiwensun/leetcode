# This is a solution to a modified question: what if the cost of each rotation is the numeric value displayed after the rotation?
import heapq

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def adjacents(state):
            return [state[:digit] + str(((int(state[digit])) + diff) % 10) + state[digit + 1:] for diff in [1, -1] for digit in range(len(state))]
        START = "0000"
        deadends = set(deadends)
        if START in deadends or target in deadends:
            return -1
        if START == target:
            return 0
        visited = { START }
        queue = [[0, START]]
        while queue:
            cost, state = heapq.heappop(queue)
            for adjacent_state in adjacents(state):
                if adjacent_state in deadends or adjacent_state in visited:
                    continue
                new_cost = cost + int(target)
                if adjacent_state == target:
                    return new_cost
                heapq.heappush(queue, [new_cost, adjacent_state])
                visited.add(adjacent_state)

        return -1

