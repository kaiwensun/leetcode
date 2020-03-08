# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def zigZagLength(root, is_left):
            if root is None:
                return 0
            direct = "left" if is_left else "right"
            attr = "_" + direct
            if getattr(root, attr, None) is None:
                setattr(root, attr, zigZagLength(getattr(root, direct), not is_left) + 1)
            return getattr(root, attr)
        def dfs(root):
            if root is None:
                return 0
            return max(zigZagLength(root, True),
                       zigZagLength(root, False),
                       dfs(root.left),
                       dfs(root.right))
        return dfs(root) - 1
