# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root, isTop=True):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return float('-inf')
        if isTop:
            self.result = root.val        
        left = self.maxPathSum(root.left, False)
        right = self.maxPathSum(root.right, False)
        rtn = max(left + root.val, right + root.val, root.val)
        self.result = max(self.result, left + right + root.val, rtn)
        if isTop:
            return self.result
        return rtn
