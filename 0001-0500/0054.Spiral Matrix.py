"""
Basic idea:
	Focus on only the part of matrix that have not been collected to the result
	recursively solve the uncollected part of matrix
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        try:
            self.collectOneLine(matrix,0,0,len(matrix[0]),0,len(matrix),res)
        except IndexError:
            pass
        return res
        
    def collectOneLine(self,matrix,direction,left,right,top,bottom,res):
        if right==left or bottom==top:
            return
        if direction==0:
            res+=matrix[top][left:right]
            top+=1
        elif direction==1:
            for i in xrange(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
        elif direction==2:
            res+=matrix[bottom-1][right-1:left-1 if left>0 else None:-1]
            bottom-=1
        else:
            for i in xrange(bottom-1,top-1 if top>0 else None,-1):
                res.append(matrix[i][left])
            left+=1
        self.collectOneLine(matrix,(direction+1)%4,left,right,top,bottom,res)

