# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rval = self.helper(root)
        return rval[0] + (1 if rval[2] else 0)
        
    def helper(self, root):
        if root is None:
            # (num of camera, am I monitoring parent, please monitor me)
            return (0, False, False)
        left = self.helper(root.left)
        right = self.helper(root.right)
        camera = left[2] or right[2]
        please_monitor_me = not camera and not(left[1] or right[1])
        return (left[0] + right[0] + (1 if camera else 0), camera, please_monitor_me)
            
