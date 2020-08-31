# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        self.helper(head)
        return reversed(self.rval)
    
    def helper(self, head):
        if head is None:
            self.stack = [0]
            self.rval = []
            return
        self.helper(head.next)
        while len(self.stack) > 1 and head.val >= self.stack[-1]:
            self.stack.pop()
        self.rval.append(self.stack[-1])
        self.stack.append(head.val)
