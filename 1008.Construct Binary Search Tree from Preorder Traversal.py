# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        dummy = TreeNode(float('inf'))
        path = [dummy]
        pointer = dummy
        for val in preorder:
            if val < pointer.val:
                pointer.left = TreeNode(val)
                path.append(pointer)
                pointer = pointer.left
            else:
                while val >= path[-1].val:
                    pointer = path.pop()
                if val < pointer.val:
                    pointer.left = TreeNode(val)
                    path.append(pointer)
                    pointer = pointer.left
                else:
                    pointer.right = TreeNode(val)
                    pointer = pointer.right
        return dummy.left
                
