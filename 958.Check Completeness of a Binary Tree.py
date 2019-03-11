# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)[0]
        
    def helper(self, root):
        # return (possible, min depth, max depth)
        if root is None:
            return True, 0, 0
        left = self.helper(root.left)
        if left[0] is False:
            return left
        right = self.helper(root.right)
        if right[0] is False:
            return right
        if right[2] > left[1]:
            return False, None, None
        if right[1] < left[2] - 1:
            return False, None, None
        minimum = right[1]
        maximum = left[2]
        return True, minimum + 1, maximum + 1
        
            
        
        
