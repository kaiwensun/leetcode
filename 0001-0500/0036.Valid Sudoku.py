class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=self.init()
        col=self.init()
        mat=self.init()
        for i in xrange(9):
            for j in xrange(9):
                c = board[i][j]
                if c!='.':
                    c=ord(c)-ord('1')
                    if row[i][c] or col[j][c] or mat[i/3*3+j/3][c]:
                        return False;
                    row[i][c]=col[j][c]=mat[i/3*3+j/3][c]=True
        return True
    def init(slef):
        array = [[]]*9
        for i in xrange(9):
            array[i]=[False]*9
        return array

s=Solution()
sin = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
s.isValidSudoku(sin)
