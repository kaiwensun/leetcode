DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))

class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def inboard(i, j):
            return 0 <= i < m and 0 <= j < n

        def check(i, j, di, dj):
            endi, endj = i + di * (len(word) - 1), j + dj * (len(word) - 1)
            if not inboard(endi, endj):
                return False
            for k in range(len(word)):
                if board[i][j] != " " and board[i][j] != word[k]:
                    return False
                i += di
                j += dj
            return not inboard(i, j) or board[i][j] == "#"

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "#":
                    continue
                for di, dj in DELTAS:
                    x, y = i - di, j - dj
                    if not inboard(x, y) or board[x][y] == "#":
                        if check(i, j, di, dj):
                            return True
        return False

