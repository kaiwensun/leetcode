import collections

def freeze(state):
    return tuple(map(tuple, state))
def unfreeze(state):
    return list(map(list, state))

DELTA = [1, 0, -1, 0, 1]
def neighbors(i, j):
    for k in range(4):
        x, y = i + DELTA[k], j + DELTA[k + 1]
        if 0 <= x < 3 and 0 <= y < 3:
            yield x, y
def moves(state):
    state = unfreeze(state)
    for i in range(3):
        for j in range(3):
            if state[i][j] > 0:
                state[i][j] -= 1
                for x, y in neighbors(i, j):
                    state[x][y] += 1
                    yield freeze(state)
                    state[x][y] -= 1
                state[i][j] += 1

target = [[1] * 3] * 3
dist = {freeze(target): 0}
queue = collections.deque([freeze(target), None])
step = 1
while len(queue) > 1:
    state = queue.popleft()
    if state is None:
        step += 1
        queue.append(state)
        continue
    for nxt in moves(state):
        if nxt in dist:
            continue
        dist[nxt] = step
        queue.append(nxt)
        
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        return dist[freeze(grid)]

