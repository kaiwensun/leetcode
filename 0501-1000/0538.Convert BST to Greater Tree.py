# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.acc = 0
        self.convert(root)
        return root
        
    def convert(self, root):
        if root is not None:
            self.convert(root.right)
            self.acc += root.val
            root.val = self.acc
            self.convert(root.left)
