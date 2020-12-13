class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        new_cuboids = []
        new_counts = []
        for cuboid in sorted(cuboids):
            if new_cuboids and cuboid == new_cuboids[-1]:
                new_counts[-1] += 1
            else:
                new_cuboids.append(cuboid)
                new_counts.append(1)
        cuboids = new_cuboids
        graph = defaultdict(list)
        for i, bigger in enumerate(cuboids):
            for j, smaller in enumerate(cuboids):
                if i == j:
                    continue
                for k in range(3):
                    if smaller[k] > bigger[k]:
                        break
                else:
                    graph[i].append(j)
        
        @lru_cache
        def dfs(i):
            res = 0
            height = cuboids[i][-1] * new_counts[i]
            for j in graph[i]:
                res = max(res, dfs(j))
            return res + height
        res = 0
        for start in range(len(cuboids)):
            res = max(res, dfs(start))
        return res

