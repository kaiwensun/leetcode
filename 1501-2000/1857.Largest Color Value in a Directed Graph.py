import collections, functools

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    
        # build graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        node_cnt = len(colors)

        visited = set()
        @functools.lru_cache(None)
        def has_cycle(u):
            if u in visited:
                return True
            visited.add(u)
            for v in graph[u]:
                if has_cycle(v):
                    return True
            visited.remove(u)
            return False
        
        # detect cycle
        for node in range(node_cnt):
            if has_cycle(node):
                return -1

        def color2index(color):
            return ord(color) - ord('a')

        @functools.lru_cache(None)
        def dfs_graph(u):
            print(u)
            mx_res = [0] * 26
            for v in graph[u]:
                res = dfs_graph(v)
                for i in range(len(mx_res)):
                    mx_res[i] = max(mx_res[i], res[i])
            mx_res[color2index(colors[u])] += 1
            return mx_res
        
        @functools.lru_cache(None)
        def dfs_reversed_graph(v):
            mx_res = [0] * 26
            for u in reversed_graph[v]:
                res = dfs_reversed_graph(u)
                for i in range(len(mx_res)):
                    mx_res[i] = max(mx_res[i], res[i])
            mx_res[color2index(colors[v])] += 1
            return mx_res

        # build reversed graph
        reversed_graph = collections.defaultdict(list)
        for u, v in edges:
            reversed_graph[v].append(u)

        # combine cnt from graph & reversed_graph
        res = 0
        for node in range(node_cnt):
            cnt1 = dfs_graph(node)
            cnt2 = dfs_reversed_graph(node)
            for i in range(len(cnt1)):
                res = max(res, cnt1[i] + cnt2[i] - (1 if color2index(colors[node]) == i else 0))
        return res

