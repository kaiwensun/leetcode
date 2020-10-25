# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def buildSubTree(pre_l, in_l, size):
            if size != 0:
                root_val = preorder[pre_l]
                inorder_index = inorder_num2index[root_val]
                lSize = inorder_index - in_l
                return TreeNode(root_val,
                                buildSubTree(pre_l + 1, in_l, lSize),
                                buildSubTree(pre_l + 1 + lSize, inorder_index + 1, size - lSize - 1)
                               )
        
        inorder_num2index={num: index for index, num in enumerate(inorder)}
        return buildSubTree(0, 0, len(preorder))

