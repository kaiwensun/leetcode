# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter

class Solution(object):
    def pathSum(self, root, sm, prefix=None):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res = 0
        if root:
            if prefix is None:
                prefix = 0
                self.seen = Counter()
                self.seen[0] = 1
            prefix += root.val
            wanted = prefix - sm
            res += self.seen[wanted]
            self.seen[prefix] += 1
            res += self.pathSum(root.left, sm, prefix)
            res += self.pathSum(root.right, sm, prefix)
            self.seen[prefix] -= 1
        return res

