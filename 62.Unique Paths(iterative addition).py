class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m>n:
            tmp=m;m=n;n=tmp;
        table = [1]*m
        lastline = [1]*m
        for row in xrange(1,m):
            for col in xrange(row,m):
                table[col]=table[col]+table[col if col==row else col-1]
            lastline[row]=table[m-1]
        for i in xrange(m,n):
            for row in xrange(1,m):
                lastline[row]=lastline[row]+lastline[row-1]
        try:
            return lastline[m-1]
        except IndexError:
            return 0
            

