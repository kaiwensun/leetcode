class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rows = {}
        cols = {}
        tl2rb = {}
        tr2lb = {}

        def tl2rbIndex(x, y, N):
            return N - x + y
        def tr2lbIndex(x, y, N):
            return x + y
        def doQuery(x, y):
            answer = 1 if isBright(x, y) else 0
            for i in xrange(x - 1, x + 2):
                for j in xrange(y - 1, y + 2):
                    turnOff(i, j)
            return answer
        def turnOff(x, y):
            if x >=0 and x < N and y >= 0 and y < N:
                rows.setdefault(x, set()).discard(y)
                cols.setdefault(y, set()).discard(x)
                tl2rb.setdefault(tl2rbIndex(x, y, N), set()).discard(y)
                tr2lb.setdefault(tr2lbIndex(x, y, N), set()).discard(y)

        def isBright(x, y):
            return rows.get(x) or cols.get(y) or tl2rb.get(tl2rbIndex(x, y, N)) or tr2lb.get(tr2lbIndex(x, y, N))
        def printBoard():
            print 'rows:', rows
            print 'cols:', cols
            print 'tl2rb:', tl2rb
            print 'tr2lb:', tr2lb
            print '=' * 20

        for x, y in lamps:
            rows.setdefault(x, set()).add(y)
            cols.setdefault(y, set()).add(x)
            tl2rb.setdefault(tl2rbIndex(x, y, N), set()).add(y)
            tr2lb.setdefault(tr2lbIndex(x, y, N), set()).add(y)
        answers = [None] * len(queries)
        # printBoard()
        for i in xrange(len(queries)):
            x, y = queries[i]
            # print 'query', queries[i], tl2rbIndex(x, y, N), tr2lbIndex(x, y, N)
            answers[i] = doQuery(*queries[i])
            # printBoard()
        return answers
            
