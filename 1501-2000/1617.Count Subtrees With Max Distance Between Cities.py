from functools import lru_cache
from collections import defaultdict

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
            
        def each_one_bit(binary):
            while binary:
                next_binary = binary & binary - 1
                yield binary - next_binary  # yield the right-most bit 1 of `binary`
                binary = next_binary

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
            return depth + 1, max_res  # (max depth, max diameter)

        @lru_cache(1 << n)  # do not search a same subtree again
        def expand_tree(subtree):
            _, max_res = get_diameter(subtree - ((subtree - 1) & subtree), subtree, 0)  # find the diameter of the subtree, by DFS from the smallest node
            res[max_res] += 1
            for shift in range(n):
                candidate = 1 << shift  # candidate to expand from the subtree
                if candidate & subtree != 0:
                    continue  # already in subtree
                candidate_neighbors = graph[candidate]
                if candidate_neighbors & subtree == 0:
                    continue  # not connected
                expand_tree(subtree | candidate)
                
        # make graph
        graph = defaultdict(int)
        for u, v in edges:
            graph[1 << (u - 1)] |= 1 << (v - 1)
            graph[1 << (v - 1)] |= 1 << (u - 1)
        res = [0] * n
        # expand subtrees from each single node
        for shift in range(n):
            expand_tree(1 << shift)
        return res[1:]

