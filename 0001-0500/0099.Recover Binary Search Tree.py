# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def discover_nodes(node):
            if node:
                discover_nodes(node.left)
                values.append(node.val)
                discover_nodes(node.right)

        def correct(root, it):
            if root:
                correct(root.left, it)
                root.val = next(it)
                correct(root.right, it)

        values = []
        discover_nodes(root)
        values.sort()
        correct(root, iter(values))

