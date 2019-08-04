# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        
        def dfs(root, stop):
            if root is None:
                return None, 0
            if root.val == stop:
                return root, 0
            left = dfs(root.left, stop)
            right = dfs(root.right, stop)
            return left[0] or right[0], left[1] + right[1] + 1
        x_node, root_cnt = dfs(root, x)
        left_cnt = dfs(x_node.left, None)[1]
        right_cnt = dfs(x_node.right, None)[1]
        return max(root_cnt, left_cnt, right_cnt) > n / 2
