# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from heapq import nlargest
from collections import Counter

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sm = Counter()
        def dfs(root, depth):
            if root:
                sm[depth] += root.val
                dfs(root.left, depth + 1)
                dfs(root.right, depth + 1)
        dfs(root, 0)
        if len(sm) < k:
            return -1
        return sorted(sm.values())[-k]

