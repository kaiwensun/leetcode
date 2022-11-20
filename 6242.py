# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import bisect

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                arr.append(node.val)
                dfs(node.right)
        dfs(root)
        def work(val):
            i = bisect.bisect_right(arr, val) - 1
            j = bisect.bisect_left(arr, val)
            return [
                arr[i] if i >= 0 else -1,
                arr[j] if j < len(arr) else -1
            ]
        return [work(query) for query in queries]

