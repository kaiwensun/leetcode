# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if root is None:
                return (None, 0)
            left = helper(root.left)
            right = helper(root.right)
            if left[0] == right[0] == root.val:
                res = left[1] + right[1] + 2
                child_path = max(left[1], right[1]) + 1
            elif left[0] == root.val:
                res = left[1] + 1
                child_path = left[1] + 1
            elif right[0] == root.val:
                res = right[1] + 1
                child_path = right[1] + 1
            else:
                res = 0
                child_path = 0
            self.res = max(self.res, res)
            return (root.val, child_path)
        helper(root)
        return self.res
