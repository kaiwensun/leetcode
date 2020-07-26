class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        visited = {(r0, c0)}
        queue = [(r0, c0)]
        pointer = 0
        while pointer < len(queue):
            cur = queue[pointer]
            pointer += 1
            for adjacent in self.adjacent(R, C, cur[0], cur[1]):
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(adjacent)
        return queue
        
        
    def adjacent(self, R, C, r, c):
        delta = (1, 0, -1, 0, 1)
        return [(r + delta[i], c + delta[i + 1]) for i in xrange(4) if 0 <= r + delta[i] < R and 0 <= c + delta[i + 1] < C]
