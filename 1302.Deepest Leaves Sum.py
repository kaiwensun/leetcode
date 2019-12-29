# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def walk(root, level):
            if not root:
                return None, float("-inf")
            if not root.left and not root.right:
                return root.val, level
            left = walk(root.left, level + 1)
            right = walk(root.right, level + 1)
            if left[1] == right[1]:
                return left[0] + right[0], left[1]
            elif left[1] > right[1]:
                return left
            else:
                return right
        return walk(root, 0)[0]
