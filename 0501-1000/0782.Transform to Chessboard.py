class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not self.isPossible(board):
            return -1
        return self.cntMove(board[0]) + self.cntMove([row[0] for row in board ])
    
    def possibleCnt(self, length):
        if length % 2:
            return [length / 2, length / 2 + 1]
        else:
            return [length / 2]
    
    def isPossible(self, board):
        cnt = 0
        for i in xrange(1, len(board)):
            diff = abs(board[0][0] - board[i][0])
            cnt += diff
            for j in xrange(1, len(board[0])):
                if diff != abs(board[0][j] - board[i][j]):
                    return False
        if cnt not in self.possibleCnt(len(board)):
            return False
        cnt = 0
        for j in xrange(1, len(board[0])):
            diff = abs(board[0][0] - board[0][j])
            cnt += diff
            for i in xrange(1, len(board)):
                if diff != abs(board[i][0] - board[i][j]):
                    return False
        if cnt not in self.possibleCnt(len(board[0])):
            return False
        return True
            
    def cntMove(self, row):
        if len(row) % 2 == 0:
            target = len(row) / 2
            ones = sum(row[::2])
            return min(target - ones, ones)
        else:
            ones = sum(row)
            if ones == len(row) / 2:
                return ones - sum(row[1::2])
            else:
                return ones - sum(row[::2])
        return rval
