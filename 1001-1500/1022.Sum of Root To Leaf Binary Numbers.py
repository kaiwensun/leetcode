# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    MOD = 10**9 + 7
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, parent):
        if root is None:
            return parent % self.MOD
        val = ((parent << 1) + root.val) % self.MOD
        if (root.left or root.right) is None:
            return val
        if (root.left and root.right) is None:
            return self.dfs(root.left or root.right, val)
        left = self.dfs(root.left, val)
        right = self.dfs(root.right, val)
        return (left + right) % self.MOD
