# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None:
            return 0
        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.res += abs(l - r)
        return l + r + node.val
