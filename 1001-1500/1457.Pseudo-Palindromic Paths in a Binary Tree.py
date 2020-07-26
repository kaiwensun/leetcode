# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        cnt = Counter()
        oddcnt = 0
        res = 0
        def dfs(root):
            nonlocal res
            nonlocal oddcnt
            if root is None:
                return
            cnt[root.val] += 1
            oddcnt += 1 if cnt[root.val] % 2 == 1 else -1
            if root.left == root.right == None:
                if oddcnt <= 1:
                    res += 1
            else:
                dfs(root.left)
                dfs(root.right)
            oddcnt -= 1 if cnt[root.val] % 2 == 1 else -1
            cnt[root.val] -= 1
        dfs(root)
        return res
