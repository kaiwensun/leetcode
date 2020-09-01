# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def getMin(root):
            while root and root.left:
                root = root.left
            return root

        if root:
            if root.val == key:
                mn = getMin(root.right)
                if mn:
                    root.val = mn.val
                    root.right = self.deleteNode(root.right, mn.val)
                else:
                    root = root.left
            elif root.val < key:
                root.right = self.deleteNode(root.right, key)
            else:
                root.left = self.deleteNode(root.left, key)
        return root
