from functools import lru_cache
from collections import defaultdict
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
            
        def each_one_bit(binary):
            while binary:
                nextBinary = binary & binary - 1
                yield binary - nextBinary
                binary = nextBinary

        def get_diameter(node, subtree, frm):
            depth = max_res = 0
            for neighbor in each_one_bit(graph[node]):
                if neighbor == frm:
                    continue  # do not go back
                if neighbor & subtree == 0:
                    continue  # neighbor not in subtree
                this_depth, this_max_res = get_diameter(neighbor, subtree, node)
                max_res = max(max_res, this_max_res, depth + this_depth)
                depth = max(depth, this_depth)
            return depth + 1, max_res
        
        
        @lru_cache(1 << n)
        def dfs(subtree):
            _, max_res = get_diameter(subtree - ((subtree - 1) & subtree), subtree, 0)
            res[max_res] += 1
            for shift in range(n):
                candidate = 1 << shift
                if candidate & subtree != 0:
                    continue  # already in subtree
                candidate_neighbors = graph[candidate]
                if candidate_neighbors & subtree == 0:
                    continue  # not connected
                dfs(subtree | candidate)
                
        graph = defaultdict(int)
        for u, v in edges:
            graph[1 << (u - 1)] |= 1 << (v - 1)
            graph[1 << (v - 1)] |= 1 << (u - 1)
        res = [0] * n
        for shift in range(n):
            dfs(1 << shift)
        return res[1:]

