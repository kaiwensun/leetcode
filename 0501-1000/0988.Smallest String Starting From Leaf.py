# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root, path=[]):
        """
        :type root: TreeNode
        :rtype: str
        """
        path.append(chr(ord('a') + root.val))
        if not root.left and not root.right:
            res = "".join(reversed(path))
        elif not root.left or not root.right:
            res = self.smallestFromLeaf(root.left or root.right, path)
        else:
            res = min(self.smallestFromLeaf(root.left, path), self.smallestFromLeaf(root.right, path))
        path.pop()
        return res

