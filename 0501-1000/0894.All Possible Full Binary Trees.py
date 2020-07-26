# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import functools
class Solution:
    @functools.lru_cache(None)
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # Definition for a binary tree node.
        if N == 1:
            return [TreeNode(0)]
        rval = []
        for left_cnt in range(1, N - 1, 2):
            left_possibles = self.allPossibleFBT(left_cnt)
            right_possibles = self.allPossibleFBT(N - 1 - left_cnt)
            for left in left_possibles:
                for right in right_possibles:
                    root = TreeNode(0)
                    root.left, root.right = left, right
                    rval.append(root)
        return rval
