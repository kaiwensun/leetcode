# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        
        def genTree(prePtr, postPtr, limit):
            if pre[prePtr] == post[postPtr]:
                return TreeNode(pre[prePtr]), 1
            root = TreeNode(pre[prePtr])
            root.left, leftSize = genTree(prePtr + 1, postPtr, limit - 1)
            if root.val == post[postPtr + leftSize]:
                rightSize = 0
            else:
                root.right, rightSize = genTree(prePtr + 1 + leftSize, postPtr + leftSize, limit - 1)
            return root, leftSize + rightSize + 1

        return genTree(0, 0, len(pre))[0]
