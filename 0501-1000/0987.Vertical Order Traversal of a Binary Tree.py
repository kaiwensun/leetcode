# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        M = {}
        left_most = self.dfs(root, 0, 0, M)
        result = []
        for x in xrange(left_most, left_most + len(M)):
            x_result = []
            for y in sorted(M[x].keys(), reverse=True):
                vals = M[x][y]
                x_result.extend(sorted(vals))
            result.append(x_result)
        return result
        
        
    def dfs(self, root, x, y, M):
        M.setdefault(x, {}).setdefault(y, [])
        M[x][y].append(root.val)
        l, r = x, x
        if root.left:
            l = self.dfs(root.left, x - 1, y - 1, M)
        if root.right:
            r = self.dfs(root.right, x + 1, y - 1, M)
        return min(l, r)

