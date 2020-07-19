import collections
class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        def dfs(root, parent):
            cnt = Counter()
            if root is not None:
                for child in graph[root]:
                    if child == parent:
                        continue
                    cnt += dfs(child, root)
                cnt[labels[root]] += 1
                res[root] = cnt[labels[root]]
            return cnt
        
        res = [None] * n
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return res
