class Solution(object):
    def isInBoard(self, x, y):
        return x >= 0 and x < 8 and y >= 0 and y < 8

    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in xrange(8):
            for j in xrange(8):
                if board[i][j] == 'R':
                    ri = i
                    rj = j
                    break
        for move in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x, y = ri + move[0], rj + move[1]
            while self.isInBoard(x, y):
                if board[x][y] == '.':
                    x += move[0]
                    y += move[1]
                    continue
                if board[x][y] == 'p':
                    result += 1
                break
        return result
                
                    
            
