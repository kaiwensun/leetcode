# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
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

