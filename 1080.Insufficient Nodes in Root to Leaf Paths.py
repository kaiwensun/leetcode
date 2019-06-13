# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(root, s):
            if root is None:
                return None
            left = dfs(root.left, s + root.val)
            right = dfs(root.right, s + root.val)
            if root.left or root.right:
                res = (left or right) and root
            else:
                res = None if s + root.val < limit else root
            root.left, root.right = left, right
            return res
        return dfs(root, 0)
