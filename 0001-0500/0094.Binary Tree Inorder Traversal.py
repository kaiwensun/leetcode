# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        0: before visiting left
        1: before visiting right
        2: finish visiting right
        """
        res = []
        stack = [(root, False)] if root else [] # 1 means ask parent to check right node
        while stack:
            node, check = stack[-1]
            if node is None:
                stack.pop()
                continue
            if check:
                res.append(node.val)
                stack.pop()
                stack.append((node.right, False))
            else:    
                stack[-1] = (node, True)
                stack.append((node.left, False))
        return res
