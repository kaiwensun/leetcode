# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        
        def genTree(head, size):
            if size == 1:
                return TreeNode(head.val), head.next
            if size == 0:
                return None, head
            leftSize = size / 2
            leftRes = genTree(head, leftSize)
            node = TreeNode(leftRes[1].val)
            node.left = leftRes[0]
            rightSize = size - leftSize - 1
            rightRes = genTree(leftRes[1].next, rightSize)
            node.right = rightRes[0]
            return node, rightRes[1]
        def getSize(head):
            cnt = 0
            while head:
                head = head.next
                cnt += 1
            return cnt
        return genTree(head, getSize(head))[0]
