"""
80ms, Your runtime beats 94.77% of python submissions.
72ms, Your runtime beats 100.00% of python submissions.
Basic idea:
	bruteforce search, set flag of placement (column, diagonals)
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        answer_collector = []
        board = [-1]*n   #board[i]==j means the i-th row has a Q at col j
        flag_col=[False]*n
        flag_dec=[False]*(2*n-1)    #diag \
        flag_inc=[False]*(2*n-1)    #diag /
        self.placeQatRow(0,flag_col,flag_dec,flag_inc,board,answer_collector,n)
        return answer_collector

    def placeQatRow(self,row,flag_col,flag_dec,flag_inc,board,answer_collector,n):
        if row==n:
            self.construct_solution(answer_collector,board,n)
            return
        for col in xrange(n):
            if flag_col[col] or flag_dec[n-1-row+col] or flag_inc[row+col]:
                continue
            else:
                board[row]=col
                flag_col[col]=True
                flag_dec[n-1-row+col]=True
                flag_inc[row+col]=True
                self.placeQatRow(row+1,flag_col,flag_dec,flag_inc,board,answer_collector,n)
                board[row]=-1
                flag_col[col]=False
                flag_dec[n-1-row+col]=False
                flag_inc[row+col]=False
        return
    
    def construct_solution(self,answer_collector,board,n):
        sol = [['.']*n for i in xrange(n)]
        for row in xrange(n):
            sol[row][board[row]]='Q'
            sol[row]="".join(sol[row])
        answer_collector.append(sol)

s = Solution()
sol = s.solveNQueens(4)
for i in xrange(len(sol)):
	print '=== %d ==='%i
	for r in xrange(len(sol[0])):
		print sol[i][r]
