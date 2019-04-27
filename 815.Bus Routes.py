class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0
        stop2route = collections.defaultdict(set)
        route2stop = {}
        for i, route in enumerate(routes):
            for stop in route:
                stop2route[stop].add(i)
            route2stop[i] = route
        queue = collections.deque([S, '#'])
        visited = {S}
        res = 0
        while len(queue) > 1:
            stop = queue.popleft()
            if stop == '#':
                res += 1
                queue.append('#')
                continue
            routes = stop2route[stop]
            neighbors = set()
            for route in routes:
                for stop in route2stop[route]:
                    if stop == T:
                        return res + 1
                    if stop not in visited:
                        neighbors.add(stop)
            visited |= neighbors
            queue.extend(neighbors)
        return -1
