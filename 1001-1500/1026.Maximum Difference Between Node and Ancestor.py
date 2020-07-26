# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root, is_root=True):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return (best_V, minimum, maximum)
        if root is None:
            return (0, None, None)
        left = self.maxAncestorDiff(root.left, False)
        right = self.maxAncestorDiff(root.right, False)
        val = root.val
        V = max(
            abs(val - left[1]) if left[1] is not None else 0,
            abs(val - left[2]) if left[2] is not None else 0,
            abs(val - right[1]) if right[1] is not None else 0,
            abs(val - right[2]) if right[2] is not None else 0)
        best_V = max(V, left[0], right[0])
        if is_root:
            return best_V
        minimum = min(left[1] if left[1] is not None else val, right[1] if right[1] is not None else val, val)
        maximum = max(left[2] if left[2] is not None else val, right[2] if right[2] is not None else val, val)
        return (best_V, minimum, maximum)
