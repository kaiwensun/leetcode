class Solution(object):
    def makeDenseMap(self, dim, blocked, source, target):
        points = blocked + [source, target]
        X = sorted([p[dim] for p in points])
        mapping = {}
        index = -1
        for x in X:
            if x not in mapping:
                index += 1 if x - 1 in mapping or x == 0 else 2
                mapping[x] = index
        source[dim] = mapping[source[dim]]
        target[dim] = mapping[target[dim]]
        for b in blocked:
            b[dim] = mapping[b[dim]]
        self.size[dim] = index
        if 999999 not in mapping:
            self.size[dim] += 1
    
    def isValid(self, point):
        return all(0 <= point[dim] <= self.size[dim] for dim in (0, 1))

    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        self.size = [None] * 2
        for dim in (0, 1):
            self.makeDenseMap(dim, blocked, source, target)
        blocked = set(map(tuple, blocked))
        source = tuple(source)
        target = tuple(target)
        queue = collections.deque([source])
        while queue:
            p = queue.popleft()
            delta = (1, 0, -1, 0, 1)
            for i in xrange(4):
                next_point = p[0] + delta[i], p[1] + delta[i + 1]
                if next_point == target:
                    return True
                if self.isValid(next_point) and next_point not in blocked:
                    blocked.add(next_point)
                    queue.append(next_point)
        return False
