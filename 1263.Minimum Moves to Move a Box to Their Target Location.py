class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        def isFree(point):
            x, y = point
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and getGrid(point) == '.'
        
        def setGrid(point, val):
            grid[point[0]][point[1]] = val
        def getGrid(point):
            return grid[point[0]][point[1]]
        
        def find(c):
            for x in range(len(grid)):
                for y in range(len(grid[0])):
                    if grid[x][y] == c:
                        grid[x][y] = '.'
                        return x, y
        
        def canGoTo(src, dst, box):
            if src == dst:
                return True
            go_cur = {src}
            go_visited = set()
            while go_cur:
                go_visited |= go_cur
                new_cur = set()
                for point in go_cur:
                    for i in range(4):
                        dx, dy = delta[i], delta[i + 1]
                        new_point = (point[0] + dx, point[1] + dy)
                        if new_point != box and isFree(new_point) and new_point not in go_visited:
                            if new_point == dst:
                                return True
                            new_cur.add(new_point)
                go_cur = new_cur
                if dst in new_cur:
                    return True
            return False
    
        delta = [1, 0, -1, 0, 1]
        target = find("T")
        player = find("S")
        box = find("B")
        if target == box:
            return 0
        
        visited = set()
        cur = {(player, box)}
        res = 0
        while cur:
            visited |= cur
            new_cur = set()
            for (player, box) in cur:
                for i in range(4):
                    dx, dy = delta[i], delta[i + 1]
                    pusher = (box[0] - dx, box[1] - dy)
                    new_box = (box[0] + dx, box[1] + dy)
                    if isFree(new_box) and (pusher, new_box) not in visited and canGoTo(player, pusher, box):
                        if new_box == target:
                            return res + 1
                        new_cur.add((pusher, new_box))
            res += 1
            cur = new_cur
        return -1
        
