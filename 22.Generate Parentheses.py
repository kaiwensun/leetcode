class Solution(object):
    MyList=[]

    def generateParenthesis(self, n):
        """
        :type n: int
        :rt ype: List[str]
        """
        self.MyList=[]
        self.n=n
        self.flushParenthesis([],0,0)
        return self.MyList

    def flushParenthesis(self,prefix,nleft,nright):
        if nleft==self.n:
            self.MyList.append("".join(prefix)+')'*(self.n-nright))
            return
        pre1=list(prefix)
        pre1.append('(')
        self.flushParenthesis(pre1,nleft+1,nright)
        if nleft>nright:
            prefix.append(')')
            self.flushParenthesis(prefix,nleft,nright+1)

