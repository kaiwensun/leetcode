from functools import lru_cache
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.parent = parent

    @lru_cache(None)
    def dp(self, node, k):
        return self.getKthAncestor(node, k)

    def getKthAncestor(self, node: int, k: int) -> int:
        if node == -1 or k == 0:
            return node
        if k == 1:
            return self.parent[node]
        highest = self.get_highest(k)
        relay = self.dp(self.dp(node, highest // 2), highest - highest // 2)
        return self.getKthAncestor(relay, k - highest)

    
    def get_highest(self, k):
        if k == 0:
            return 0
        k |= k >> 1
        k |= k >> 2
        k |= k >> 4
        k |= k >> 8
        k |= k >> 16
        return (k + 1) >> 1

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
