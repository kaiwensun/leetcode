# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
          
        def dfs(root):
            nonlocal res
            if root is None:
                return [0] * 11
            if root.left is None and root.right is None:
                return [0, 1] + [0] * 9
            l = dfs(root.left)
            r = dfs(root.right)
            cur, rprefix = 0, [0] * 11
            for i in range(1, 11):
                rprefix[i] = rprefix[i - 1] + r[i]
            for i in range(1, distance):
                res += l[i] * rprefix[distance - i]
            for i in range(10, 0, -1):
                l[i] = l[i - 1] + r[i - 1]
            return l

        res = 0
        dfs(root)
        return res