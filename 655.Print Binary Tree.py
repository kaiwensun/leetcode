# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def getSize(root):
            if root is None:
                return 0, 0
            lw, lh = getSize(root.left)
            rw, rh = getSize(root.right)
            return max(lw, rw) * 2 + 1, max(lh, rh) + 1
        def fill(root, left, right, depth):
            if root is None:
                return
            mid = (left + right) / 2
            res[depth][mid] = str(root.val)
            fill(root.left, left, mid - 1, depth + 1)
            fill(root.right, mid + 1, right, depth + 1)
        w, h = getSize(root)
        res = [[""] * w for _ in xrange(h)]
        fill(root, 0, w - 1, 0)
        return res
