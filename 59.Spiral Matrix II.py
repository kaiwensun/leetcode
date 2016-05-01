"""
Basic idea:
	recursion
21 / 21 test cases passed.
Status: Accepted
Runtime: 40 ms
Your runtime beats 95.61% of python submissions.
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in xrange(n)]
        try:
            self.helper(matrix,0,len(matrix)-1,0,len(matrix[0])-1,1,0)
        except IndexError:
            pass
        return matrix
    
    def helper(self,matrix,left,right,top,bottom,start,direction):
        if right<left or bottom<top:
            return
        if direction==0:
            matrix[top][left:right+1]=xrange(start,start-left+right+1)
            start = start-left+right+1
            top+=1
        elif direction==1:
            for i in xrange(top,bottom+1):
                matrix[i][right]=start+i-top
            start = start+bottom+1-top
            right-=1
        elif direction==2:
            matrix[bottom][right:left-1 if left>0 else None:-1]=xrange(start,start-left+right+1)
            start = start-left+right+1
            bottom-=1
        else:
            for i in xrange(bottom,top-1 if top>0 else None,-1):
                matrix[i][left]=start+bottom-i
            start = start+bottom+1-top
            left+=1
        self.helper(matrix,left,right,top,bottom,start,(direction+1)%4)

