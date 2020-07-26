class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        
        ports = {
            1: 'lr',
            2: 'ud',
            3: 'ld',
            4: 'rd',
            5: 'lu',
            6: 'ur'
        }
        directs = {
            'l': (0, -1),
            'r': (0, 1),
            'u': (-1, 0),
            'd': (1, 0)
        }
        opposit_directs = {
            'l': 'r',
            'r': 'l',
            'u': 'd',
            'd': 'u'
        }
        def walk(i, j, src, visited):
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return False
            if (i, j) in visited:
                return False
            street = grid[i][j]
            if src not in ports[street]:
                return False
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return True
            for direct in ports[street]:
                if src == direct:
                    continue
                delta = directs[direct]
                visited.add((i, j))
                return walk(i + delta[0], j + delta[1], opposit_directs[direct], visited)
        
        
        for direct in ports[grid[0][0]]:
            if walk(0, 0, direct, set()):
                return True
        return False
            
            
