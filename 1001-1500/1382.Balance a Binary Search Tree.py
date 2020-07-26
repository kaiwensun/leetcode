# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)
        dfs(root)
        def buildTree(l, r):
            if l == r:
                return TreeNode(arr[l])
            if l > r:
                return None
            root_index = (l + r) / 2
            root = TreeNode(arr[root_index])
            root.left = buildTree(l, root_index - 1)
            root.right = buildTree(root_index + 1, r)
            return root
        return buildTree(0, len(arr) - 1)
            
