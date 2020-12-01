# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0, 0, 0
            l = dfs(root.left)
            r = dfs(root.right)
            coins = root.val + l[0] + r[0]
            nodes = 1 + l[1] + r[1]
            diff = abs(coins - nodes) + l[2] + r[2]
            return coins, nodes, diff

        return dfs(root)[-1]

