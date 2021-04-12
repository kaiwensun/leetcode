# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # return min, max, mindiff
        def dfs(node):
            if node is None:
                return float("inf"), float("-inf"), float("inf")
            left = dfs(node.left)
            right = dfs(node.right)
            return (
                min(node.val, left[0]),
                max(node.val, right[1]),
                min(left[2], right[2], node.val - left[1], right[0] - node.val)
            )

        return dfs(root)[-1]

