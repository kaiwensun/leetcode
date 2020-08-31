# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        def collectSubtree(root):
            if root is None:
                return 0
            left = collectSubtree(root.left)
            right = collectSubtree(root.right)
            root._left_sum = left
            root._right_sum = right
            return left + right + root.val
        def propagate(root, from_parent):
            if root is None:
                return 0
            prod = max((root.val + root._left_sum + from_parent) * root._right_sum,
                       (root.val + root._right_sum + from_parent) * root._left_sum)
            prod = max(prod, propagate(root.left, from_parent + root._right_sum + root.val))
            prod = max(prod, propagate(root.right, from_parent + root._left_sum + root.val))
            return prod
        collectSubtree(root)
        return propagate(root, 0) % MOD
                
