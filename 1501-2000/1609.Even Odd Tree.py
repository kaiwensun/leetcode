# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root, level=0, path=[]):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if level == 0:
            path = []
        if root:
            if root.val % 2 == level % 2:
                return False
            if level >= len(path):
                path.append(root.val)
            else:
                if level % 2 == 0 and path[level] >= root.val:
                    return False
                if level % 2 == 1 and path[level] <= root.val:
                    return False
                path[level] = root.val
            if not self.isEvenOddTree(root.left, level + 1, path):
                return False
            if not self.isEvenOddTree(root.right, level + 1, path):
                return False
        return True

