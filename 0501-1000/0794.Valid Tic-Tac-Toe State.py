class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        winner = None
        for b in (board, zip(*board)):
            win = 0
            for row in b:
                if len(set(row)) == 1 and row[0] != " ":
                    win += 1
                    winner = row[0]
            if win > 1:
                return False
        for opt in ((0).__add__, (2).__sub__):
            if len(set(board[i][opt(i)] for i in xrange(3))) == 1 and board[0][opt(0)] != " ":
                win += 1
                winner = board[0][opt(0)]
        
        cnt = 0
        for row in board:
            for c in row:
                if c == "X":
                    cnt += 1
                elif c == "O":
                    cnt -= 1
        if winner == "O":
            return cnt == 0
        elif winner == "X":
            return cnt == 1
        return 0 <= cnt <= 1
