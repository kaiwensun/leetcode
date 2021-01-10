# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def length(head):
            return length(head.next) + 1 if head else 0
        def get(head, k):
            if k == 1:
                return head
            else:
                return get(head.next, k - 1)
        size = length(head)
        node1 = get(head, k)
        node2 = get(head, size - k + 1)
        node1.val, node2.val = node2.val, node1.val
        return head

