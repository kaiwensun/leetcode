# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Summary = collections.namedtuple('Summary', ['isBST', 'min', 'max', 'sum', 'max_sum'])
        def dfs(root):
            if root is None:
                return Summary(True, None, None, 0, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            isBST = left.isBST and right.isBST and (left.max is None or left.max < root.val) and (right.min is None or right.min > root.val)
            sm = left.sum + right.sum + root.val
            return Summary(
                isBST,
                root.val if left.min is None else left.min,
                root.val if right.max is None else right.max,
                sm,
                max(left.max_sum, right.max_sum, int(isBST) and sm))

        return dfs(root).max_sum
