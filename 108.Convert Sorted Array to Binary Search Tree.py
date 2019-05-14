# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def helper(i, j):
            if i == j:
                return None
            mid = i + (j - i) / 2
            node = TreeNode(nums[mid])
            node.left = helper(i, mid)
            node.right = helper(mid + 1, j)
            return node
        return helper(0, len(nums))
