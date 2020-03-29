# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import functools
@functools.lru_cache(None)
def genTree(start, end):
    if start == end:
        return [None]
    else:
        res = []
        for root in range(start, end):
            for l in genTree(start, root):
                for r in genTree(root + 1, end):
                    res.append(TreeNode(root))
                    res[-1].left, res[-1].right = l, r
        return res
            
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return genTree(1, n + 1)
