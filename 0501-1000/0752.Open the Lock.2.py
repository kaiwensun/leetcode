import collections

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
        queue = collections.deque([START, "#"])
        cost = 0
        while len(queue) != 1:
            state = queue.popleft()
            if state == "#":
                queue.append("#")
                cost += 1
                continue
            for adjacent_state in adjacents(state):
                if adjacent_state in deadends or adjacent_state in visited:
                    continue
                if adjacent_state == target:
                    return cost + 1
                queue.append(adjacent_state)
                visited.add(adjacent_state)

        return -1

