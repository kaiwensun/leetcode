class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        data = list(range(n))
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                data[rx] = ry

        for u, v in edges:
            union(u, v)
            if find(start) == find(end):
                return True
        return find(start) == find(end)

