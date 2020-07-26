# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        seen = set()
        seen_twice = set()
        def dfs(root):
            if root is None:
                return None
            digest = (root.val, dfs(root.left), dfs(root.right))
            if digest in seen:
                if digest not in seen_twice:
                    seen_twice.add(digest)
                    res.append(root)
            else:
                seen.add(digest)
            return digest
        dfs(root)
        return res
