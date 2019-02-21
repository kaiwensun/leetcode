class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.NUMS = set(u'123456789')
        self.rowFlags = [set() for _ in xrange(9)]
        self.colFlags = [set() for _ in xrange(9)]
        self.boxFlags = [set() for _ in xrange(9)]
        self.initCounters()
        self.dfs(0, -1)
        
    def cord2boxId(self, r, c):
        boxRow = r // 3
        boxCol = c // 3
        return boxCol * 3 + boxRow
        
    def nextCord(self, startRow, startCol):
        startCol += 1
        for r in xrange(startRow, 9):
            for c in xrange(startCol, 9):
                if self.board[r][c] == '.':
                    return r, c
            startCol = 0
        return -1, -1
    
    def initCounters(self):
        for r in xrange(9):
            for c in xrange(9):
                n = self.board[r][c]
                self.rowFlags[r].add(n)
                self.colFlags[c].add(n)
                self.boxFlags[self.cord2boxId(r, c)].add(n)

    def dfs(self, r, c):
        r, c = self.nextCord(r, c)
        if (r, c) == (-1, -1):
            return True
        boxId = self.cord2boxId(r, c)
        candidates = self.NUMS - (self.rowFlags[r].union(self.colFlags[c]).union(self.boxFlags[boxId]))
        for candidate in candidates:
            self.rowFlags[r].add(candidate)
            self.colFlags[c].add(candidate)
            self.boxFlags[boxId].add(candidate)
            found = self.dfs(r, c)
            if found:
                self.board[r][c] = candidate
                return True
            self.rowFlags[r].remove(candidate)
            self.colFlags[c].remove(candidate)
            self.boxFlags[boxId].remove(candidate)
        return False
        


        
        
    
        
        
        
    
