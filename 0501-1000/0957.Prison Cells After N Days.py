class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        self.day2state = []
        self.state2day = {}
        day = 0
        state = tuple(cell for cell in cells)
        while day <= N:
            self.day2state.append(state)
            self.state2day[state] = day
            state, old_state = self.nextState(state), state
            day += 1
            if state in self.state2day:
                break
        else:
            return old_state
        start = self.state2day[state]
        period = day - start
        return self.day2state[start + (N - start) % period]

        
    def nextState(self, cells):
        return tuple(0 if i == 0 or i == len(cells) - 1 else (cells[i - 1] + cells[i + 1] + 1) & 1 for i in xrange(len(cells)))

