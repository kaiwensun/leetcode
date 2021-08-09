class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        mid_color = 'B' if color == 'W' else 'W'
        for di in -1, 0, 1:
            for dj in -1, 0, 1:
                if di == dj == 0:
                    continue
                size = 1
                x, y = rMove + di, cMove + dj
                while 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if board[x][y] == mid_color:
                        size += 1
                        x += di
                        y += dj
                        continue
                    if size == 1 or board[x][y] == '.':
                        break
                    return True
        return False

