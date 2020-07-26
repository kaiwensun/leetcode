# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        def dfs(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = dfs(root.left, parent_exist=False)
                root.right = dfs(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = dfs(root.left, parent_exist=True)
                root.right = dfs(root.right, parent_exist=True)
                return root
        to_delete = set(to_delete)
        res = []
        dfs(root, parent_exist=False)
        return res
