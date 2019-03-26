class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        visited = set()
        queue = ["0000", "#"]
        step = 0
        while len(queue) != 1:
            state = queue.pop(0)
            if state == '#':
                step += 1
                queue.append('#')
            elif state == target:
                return step
            elif state in deadends:
                continue
            elif state in visited:
                continue
            else:
                adjacent_states = self.adjacents(state)
                for adjacent_state in adjacent_states:
                    if adjacent_state not in visited and adjacent_state not in deadends:
                        queue.append(adjacent_state)
                visited.add(state)
        return -1

    def adjacents(self, state):
        return [state[:digit] + str(((int(state[digit])) + diff) % 10) + state[digit + 1:] for diff in [1, -1] for digit in xrange(len(state))]
