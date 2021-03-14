from collections import defaultdict

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        cnt = defaultdict(set)
        for u, v in edges:
            cnt[u].add(v)
            cnt[v].add(u)
        for k, v in cnt.items():
            if len(v) == len(cnt) - 1:
                return k

