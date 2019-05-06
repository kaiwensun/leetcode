class Solution(object): 
    adjacents = {
        0: (1, 3),
        1: (0, 2, 4),
        2: (1, 5),
        3: (0, 4),
        4: (1, 3, 5),
        5: (2, 4)
    }
    cache = {123450: 0}
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        status = 0
        for row in board:
            for digit in row:
                status *= 10
                status += digit
        board = status
        if len(self.cache) > 1:
            return self.cache.get(board, -1)
        q = collections.deque([(123450, 5), (-1, -1)])
        dist = 1

        def getDigit(status, d):
            d = 5 - d
            return status / 10**d % 10
        
        def moveZero(status, from_d, to_d):
            v = getDigit(status, to_d)
            status = status - v * 10 ** (5 - to_d) + v * 10 ** (5 - from_d)
            return status
        
        def getNextStatus(status, zeroPosi):
            return ((moveZero(status, zeroPosi, to_d), to_d) for to_d in self.adjacents[zeroPosi])
        
        while len(q) > 1:
            status, zeroPosi = q.popleft()
            if status == -1:
                q.append((status, zeroPosi))
                dist += 1
                continue
            for next_status, next_zeroPosi in getNextStatus(status, zeroPosi):
                if next_status in self.cache:
                    continue
                self.cache[next_status] = dist
                q.append((next_status, next_zeroPosi))
        return self.cache.get(board, -1)
