# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        self.pointer = dummy
        self.dfs(root)
        n = dummy.right.right
        return dummy.right

        
    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.pointer.right = root
        self.pointer.left = None
        self.pointer = self.pointer.right
        self.dfs(root.right)
        self.pointer.left = None
