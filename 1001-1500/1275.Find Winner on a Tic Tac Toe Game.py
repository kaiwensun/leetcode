class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[" "] * 3 for _ in range(3)]
        player = "A"
        for move in moves:
            grid[move[0]][move[1]] = player
            player = "A" if player != "A" else "B"
        for player in "AB":
            for row in grid:
                if "".join(row) == player * 3:
                    return player
            for col in zip(*grid):
                if "".join(col) == player * 3:
                    return player
                if grid[0][0] == grid[1][1] == grid[2][2] == player:
                    return player
                if grid[0][2] == grid[1][1] == grid[2][0] == player:
                    return player
        return "Draw" if len(moves) == 9 else "Pending"
