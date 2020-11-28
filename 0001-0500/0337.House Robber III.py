# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                return root.val + left[1] + right[1], max(left) + max(right)
            else:
                return 0, 0
        return max(dfs(root))

