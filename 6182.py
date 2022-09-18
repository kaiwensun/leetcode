# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth, is_left):
            if node:
                if depth % 2:
                    yield node
                for child in dfs(node.left if is_left else node.right, depth + 1, is_left):
                    yield child
                for child in dfs(node.right if is_left else node.left, depth + 1, is_left):
                    yield child
        for left, right in zip(dfs(root.left, 1, True), dfs(root.right, 1, False)):
            left.val, right.val = right.val, left.val
        return root

