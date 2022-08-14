from collections import Counter

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        res = Counter()
        for src, dst in enumerate(edges):
            res[dst] += src
        return -max([score, -node] for node, score in res.items())[1]

