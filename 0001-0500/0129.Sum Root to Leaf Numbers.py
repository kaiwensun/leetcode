# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root, prefix=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return prefix
        prefix = root.val + prefix * 10
        if root.left is None and root.right is None:
            return prefix
        if root.left is None or root.right is None:
            return self.sumNumbers(root.left or root.right, prefix)
        return self.sumNumbers(root.left, prefix) + self.sumNumbers(root.right, prefix)
