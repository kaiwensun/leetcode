# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return 0, 0
            left, right = dfs(root.left), dfs(root.right)
            return left[0] + right[0] + (left[1] + right[1] == root.val), left[1] + right[1] + root.val
        return dfs(root)[0]

