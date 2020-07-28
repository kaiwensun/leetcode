# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def dfs():
            nonlocal i, j
            if i < 0 or j < 0:
                return None
            if inorder[i] in ancestors:
                return None
            val = postorder[j]
            root = TreeNode(val)
            ancestors.add(val)
            j -= 1
            root.right = dfs()
            if inorder[i] == val:
                i -= 1
                root.left = dfs()
            ancestors.discard(val)
            return root

        i = j = len(inorder) - 1
        ancestors = set()
        return dfs()
