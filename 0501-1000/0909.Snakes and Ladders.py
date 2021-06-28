from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        M, N = len(board), len(board[0])
        TOTAL = M * N

        def num2ij(num):
            assert(0 <= num < M * N)
            i = M - 1 - num // N
            j = num % N if num % (N * 2) < N else N - 1 - num % N
            return i, j
        
        queue = deque([0, "#"])
        visited = set()
        res = 0
        while len(queue) > 1:
            num = queue.popleft()
            if num == "#":
                res += 1
                queue.append(num)
                continue
            if num in visited:
                continue
            visited.add(num)
            for nxt in range(num + 1, min(num + 7, TOTAL)):
                x, y = num2ij(nxt)
                if board[x][y] >= 0 and nxt != TOTAL - 1:
                    nxt = board[x][y] - 1
                if nxt == TOTAL - 1:
                    return res + 1
                if nxt not in visited:
                    queue.append(nxt)
        return -1

