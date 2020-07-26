# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def walk(root):
            if root and (root.left or root.right):
                for node in (root.left, root.right):
                    for val in walk(node):
                        yield val
            elif root:
                yield root.val
        a = b = None
        gen1, gen2 = walk(root1), walk(root2)
        while a == b:
            a = next(gen1, None)
            b = next(gen2, None)
            if a != b:
                return False
            if a is None:
                return True
        assert(False)
