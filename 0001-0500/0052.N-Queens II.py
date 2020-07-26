"""
Basic idea:
	same as Prob 51. N-Queens
Another idea:
	use bitmap, bitmap switch, and only use n bits to represent the "valid" diagonals on the CURRENT row.
	see more at:
	http://gregtrowbridge.com/a-bitwise-solution-to-the-n-queens-problem-in-javascript/
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.answer_collector=0
        board = [-1]*n   #board[i]==j means the i-th row has a Q at col j
        flag_col=[False]*n
        flag_dec=[False]*(2*n-1)    #diag \
        flag_inc=[False]*(2*n-1)    #diag /
        self.placeQatRow(0,flag_col,flag_dec,flag_inc,board,n)
        return self.answer_collector
        

    def placeQatRow(self,row,flag_col,flag_dec,flag_inc,board,n):
        if row==n:
            self.answer_collector+=1
            return
        for col in xrange(n):
            if flag_col[col] or flag_dec[n-1-row+col] or flag_inc[row+col]:
                continue
            else:
                board[row]=col
                flag_col[col]=True
                flag_dec[n-1-row+col]=True
                flag_inc[row+col]=True
                self.placeQatRow(row+1,flag_col,flag_dec,flag_inc,board,n)
                board[row]=-1
                flag_col[col]=False
                flag_dec[n-1-row+col]=False
                flag_inc[row+col]=False

s = Solution()
sol = s.solveNQueens(4)
print sol
