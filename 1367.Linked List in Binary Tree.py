# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(head, root):
            if head is None or root is None:
                return head is None
            return root.val == head.val and (dfs(head.next, root.left) or dfs(head.next, root.right))
        def walkTree(root):
            if root is None:
                return False
            return dfs(head, root) or walkTree(root.left) or walkTree(root.right)
        return walkTree(root)
