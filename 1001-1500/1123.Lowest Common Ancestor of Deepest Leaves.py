# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def depth(root):
            if root is None:
                return 0
            return max(depth(root.left), depth(root.right)) + 1
        DEPTH = depth(root)
        def helper(root, your_depth):
            if your_depth == DEPTH - 1 and root is not None:
                return root
            if root is None:
                return None
            l = helper(root.left, your_depth + 1)
            r = helper(root.right, your_depth + 1)
            if l and r:
                return root
            return l or r
        return helper(root, 0)
