class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def check(i, j, di, dj):
            endi, endj = i + di * (len(word) - 1), j + dj * (len(word) - 1)
            if not (0 <= endi < m and 0 <= endj < n):
                return False
            for k in range(len(word)):
                if board[i][j] != " ":
                    if board[i][j] != word[k]:
                        return False
                i += di
                j += dj
            if (not (0 <= i < m and 0 <= j < n)) or board[i][j] == "#":
                return True
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "#":
                    continue
                deltas = []
                if i == 0 or board[i - 1][j] == "#":
                    deltas.append((1, 0))
                if i == m - 1 or board[i + 1][j] == "#":
                    deltas.append((-1, 0))
                if j == 0 or board[i][j - 1] == "#":
                    deltas.append((0, 1))
                if j == n - 1 or board[i][j + 1] == "#":
                    deltas.append((0, -1))
                for di, dj in deltas:
                    if check(i, j, di, dj):
                        return True
        return False

